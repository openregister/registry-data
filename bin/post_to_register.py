#!/usr/bin/env python3

import os
import sys
import yaml
import json
import requests

data_dirs = ['data/Register','data/re']
files_to_post = os.listdir(data_dir)
url = "%s/create" % sys.argv[1]
headers = {'Content-Type': 'application/json'}

for file in files_to_post:
    path = '%s/%s' % (data_dir, file)
    with open(path) as reg_file:
        yaml_file = yaml.load(reg_file)
        entry_json = json.dumps(yaml_file)
        print('posting', entry_json)
        res = requests.post(url, headers=headers, data=entry_json)
        print('response status_code', res.status_code)
