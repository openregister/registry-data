import os

from openregister import Item


def load_items(register):
    d = {}
    dirname = os.path.join("data", register)
    for file in os.listdir(dirname):
        if file.endswith(".yaml"):
            item = Item()
            item.yaml = open(os.path.join(dirname, file)).read()
            d[item[register]] = item
    return d


registers = load_items("register")
fields = load_items("field")
datatypes = load_items("datatype")
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
