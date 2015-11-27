import os
import pytest

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
register_fields = {}

for register in registers:
    for field in registers[register].fields:
        if field not in register_fields:
            register_fields[field] = []
        register_fields[field].append(register)


@pytest.mark.parametrize('register', registers)
def test_register(register):
    item = registers[register]
    assert item.register == register
    for field in item.keys:
        assert field in fields
        assert field in registers['register'].fields
        assert item.text == item.text.rstrip(' \n\r.')


@pytest.mark.parametrize('field', fields)
def test_field(field):
    item = fields[field]
    assert item.field == field
    for field in item.keys:
        assert field in register_fields
        assert field in registers['field'].fields
        assert item.text == item.text.rstrip()


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype(datatype):
    item = datatypes[datatype]
    assert item.datatype == datatype
    for field in item.keys:
        assert field in registers['datatype'].fields
        assert item.text == item.text.rstrip()
