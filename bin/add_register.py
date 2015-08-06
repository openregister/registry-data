#!/usr/bin/env python3

# To use this, you'll need:
#
# * boto credentials in your ~/.boto with access to the appropriate
#   route53 account.  See
#   http://docs.pythonboto.org/en/latest/getting_started.html#configuring-boto-credentials
# * heroku command line tools
# * the field.register repo checked out in the same directory as where
#   you have register.register

import argparse
import json
import os
import subprocess
import sys
import yaml

import boto.route53
import requests


FIELD_DATA_TSV_FILENAME=os.path.realpath(os.path.dirname(__file__) + '/../data/Field/fields.tsv')


def verify_all_fields_exist(register_dict):
    # this just warns, doesn't abort
    for field in register_dict['fields']:
        # we'll create this field ourselves so it doesn't matter if it
        # doesn't exist
        if field == register_dict['register']:
            continue
        field_url = "http://field.openregister.org/field/%s" % field
        r = requests.head(url=field_url)
        if r.status_code >= 400:
            print("field", field, "doesn't exist, got status", r.status_code)


def verify_field_register_data_in_expected_place():
    if not os.path.isfile(FIELD_DATA_TSV_FILENAME):
        print("Couldn't find fields.tsv at",FIELD_DATA_TSV_FILENAME)
        sys.exit()


def verify_assumptions(register_dict):
    verify_all_fields_exist(register_dict)
    verify_field_register_data_in_expected_place()


def add_cname_to_dns(name, value):
    """Adds a CNAME to route53.

    name: the fully-qualified domain name for the CNAME.  You must
    include the trailing '.' character.

    value: the domain name that the CNAME should refer to.

    """
    conn = boto.route53.connect_to_region('eu-west-1')
    zone = conn.get_zone('openregister.org.')

    status = None
    if zone.get_cname(name) != None:
        status = zone.update_cname(name, value, ttl=300)
    else:
        status = zone.add_cname(name, value, ttl=300)
    return status


def add_subdomain_to_herokuapp(subdomain, app):
    subprocess.call(['heroku','domains:add',subdomain,'--app',app])


def add_data_to_field_register_tsv(field_record):
    with open(FIELD_DATA_TSV_FILENAME, "a") as field_tsv:
        field_tsv.write("%s\t%s\t%s\t%s\t%s\n" % (
            field_record['field'],
            field_record['datatype'],
            field_record['register'],
            field_record['cardinality'],
            field_record['text']
        ))


# also this won't do anything if the field already exists
def add_field_to_field_register(register_name, record_description):
    url = 'http://field.openregister.org/create'
    headers = {'Content-type': 'application/json'}
    field_record = {
        'field': register_name,
        'datatype': 'string',
        'register': register_name,
        'cardinality': '1',
        'text': record_description
    }
    res = requests.post(url, headers=headers, data=json.dumps(field_record))

    add_data_to_field_register_tsv(field_record)
    print("""The data in field.register has been updated. You should commit and
push this to prevent losing the new field for this register.""")

    return res


def add_register_to_register_register(register_dict):
    url = 'http://register.openregister.org/create'
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, headers=headers, data=json.dumps(register_dict))
    return r


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("register_yaml", help="A yaml file describing the register.")
    parser.add_argument("herokuapp", help="The name of the herokuapp instance.  eg registry-1-openregister.")
    parser.add_argument("--record_description", help="A description of a record in the register.  For example, \"A school in the UK.\"")
    args = parser.parse_args()

    with open(args.register_yaml) as register_yaml_file:
        register_dict = yaml.load(register_yaml_file)

    register_fqdn = "%s.openregister.org" % register_dict['register']
    herokuapp_fqdn = "%s.herokuapp.com" % args.herokuapp

    verify_assumptions(register_dict)

    dns_status = add_cname_to_dns(register_fqdn + '.', herokuapp_fqdn)

    add_subdomain_to_herokuapp(register_fqdn, args.herokuapp)

    field_response = add_field_to_field_register(register_dict['register'], args.record_description)
    print('field register status code:', field_response.status_code)

    register_response = add_register_to_register_register(register_dict)
    print('register register status code:', register_response.status_code)
