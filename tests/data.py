import os

from openregister import Item


def load_data(name):
    d = {}
    dirname = os.path.join("data", name)
    for file in os.listdir(dirname):
        if file.endswith(".yaml"):
            item = Item()
            item.yaml = open(os.path.join(dirname, file)).read()
            d[item[name]] = item
    return d


registers = load_data("register")
fields = load_data("field")
datatypes = load_data("datatype")
phases = ['discovery', 'alpha', 'beta', 'live']


# reference of fields used by a register
register_fields = {}
for register in registers:
    for field in registers[register].fields:
        register_fields.setdefault(field, []).append(register)


# reference of datatypes used in a field
field_datatypes = {}
for field in fields:
    datatype = fields[field].datatype
    field_datatypes.setdefault(datatype, []).append(field)
