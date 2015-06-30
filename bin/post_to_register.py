#!/usr/bin/env python3

import os
import sys
import yaml
import json
import argparse
import requests


if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--d", help="A directory cotaining register yaml. e.g. data/Register", required=True)
    parser.add_argument("--r", help="The load url of the register to load data into. e.g. http://register.openregister.org/load", required=True)
    args = parser.parse_args()

    files_to_post = os.listdir(args.d)

    url = "%s/create" % args.r
    headers = {'Content-Type': 'application/json'}

    for file in files_to_post:
        path = '%s/%s' % (args.d, file)
        with open(path) as reg_file:
            yaml_file = yaml.load(reg_file)
            entry_json = json.dumps(yaml_file)
            res = requests.post(url, headers=headers, data=entry_json)
            if res.status_code == 202:
                print('Created, status code', res.status_code, entry_json)
            else:
                print('Not created, status code', res.status_code, entry_json)

