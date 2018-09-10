import os

from openregister import Item


REGISTRY_ENV = os.getenv('REGISTRY_ENV', "alpha")


def load_items(register):
    d = {}
    dirname = os.path.join("data", REGISTRY_ENV, register)
    for file in os.listdir(dirname):
        if file.endswith(".yaml") and file != 'meta.yaml':
            item = Item()
            item.yaml = open(os.path.join(dirname, file)).read()
            d[item[register]] = item
    return d


registers = load_items("register")
fields = load_items("field")
datatypes = load_items("datatype")
registries = load_items("registry")

phases = ['discovery', 'alpha', 'beta', 'live']


# registries referenced by a register
registry_registers = {}
for register in registers:
    registry = registers[register].registry
    registry_registers.setdefault(registry, []).append(register)


# fields referenced in a register
register_fields = {}
for register in registers:
    for field in registers[register].fields:
        register_fields.setdefault(field, []).append(register)


# datatypes referenced by a field
field_datatypes = {}
for field in fields:
    datatype = fields[field].datatype
    field_datatypes.setdefault(datatype, []).append(field)
