#!/usr/bin/env python

# create a single jsonl file from individual register entries

import sys
import os
from openregister import Item
from openregister.representations.jsonl import Writer

register = sys.argv[1] or "register"
dirname = os.path.join("data", register)

writer = Writer(sys.stdout)

for file in os.listdir(dirname):
    if file.endswith(".yaml"):
        item = Item()
        item.yaml = open(os.path.join(dirname, file)).read()
        writer.write(item)

writer.close()
