import os

from openregister import Item


def load_data(name):
    d = {}
    dirname = "data/" + name + "/"
    for file in os.listdir(dirname):
        if file.endswith(".yaml"):
            item = Item()
            item.yaml = open(dirname + file).read()
            d[item[name]] = item
    return d


registers = load_data("register")
fields = load_data("field")
datatypes = load_data("datatype")
phases = ['discovery', 'alpha', 'beta', 'live']
