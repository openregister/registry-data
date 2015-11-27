#!/usr/bin/env python

# one-off hack script to turn beta JSON-L/TSV back to individual yaml entries

from openregister.representations.jsonl import reader as jsonl_reader
from openregister.representations.tsv import reader as tsv_reader


def dump_item(register, item):
    item.phase = "alpha"
    f = open('data/' + register + '/' + item[register] + '.yaml', "w")
    f.write(item.yaml)
    f.close()


for item in jsonl_reader(open('beta/register.jsonl')):
    dump_item("register", item)

for item in tsv_reader(open('beta/field.tsv')):
    dump_item("field", item)

for item in jsonl_reader(open('beta/datatype.jsonl')):
    dump_item("datatype", item)
