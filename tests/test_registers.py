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
phases = ['discovery', 'alpha', 'beta', 'live']


@pytest.mark.parametrize('register', registers)
def test_register_key_matches_filename(register):
    assert registers[register].register == register


@pytest.mark.parametrize('field', fields)
def test_field_key_matches_filename(field):
    assert fields[field].field == field


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_key_matches_filename(datatype):
    assert datatypes[datatype].datatype == datatype


@pytest.mark.parametrize('register', registers)
def test_register_keys_are_known_fields(register):
    for field in registers[register].keys:
        assert field in fields


@pytest.mark.parametrize('field', fields)
def test_field_register_is_a_known_register(field):
    register = fields[field].register
    assert (not register) or register in registers


@pytest.mark.parametrize('field', fields)
def test_field_keys_are_known_fields(field):
    for field in fields[field].keys:
        assert field in fields


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_keys_are_known_fields(datatype):
    for field in datatypes[datatype].keys:
        assert field in fields


@pytest.mark.parametrize('register', registers)
def test_register_fields_are_register_fields(register):
    for field in registers[register].keys:
        assert field in registers['register'].fields


@pytest.mark.parametrize('field', fields)
def test_field_fields_are_register_fields(field):
    for field in fields[field].keys:
        assert field in registers['field'].fields


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_datatypes_are_register_datatypes(datatype):
    for field in datatypes[datatype].keys:
        assert field in registers['datatype'].fields


@pytest.mark.parametrize('register', registers)
def test_register_text_trailing_characters(register):
    text = registers[register].text
    assert text == text.rstrip(' \n\r.')


@pytest.mark.parametrize('field', fields)
def test_field_text_trailing_characters(field):
    text = fields[field].text
    assert text == text.rstrip(' \n\r')


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_text_trailing_characters(datatype):
    text = datatypes[datatype].text
    assert text == text.rstrip(' \n\r')


@pytest.mark.parametrize('register', registers)
def test_register_fields_are_known(register):
    item = registers[register]
    for field in item.fields:
        assert field in fields


# cross-reference of fields used by a register
register_fields = {}
for register in registers:
    for field in registers[register].fields:
        if field not in register_fields:
            register_fields[field] = []
        register_fields[field].append(register)


@pytest.mark.parametrize('field', fields)
def test_field_is_used_in_a_register(field):
    assert field in register_fields


# cross-reference of datatypes used in a field
field_datatypes = {}
for field in fields:
    datatype = fields[field].datatype
    if datatype not in field_datatypes:
        field_datatypes[datatype] = []
    field_datatypes[datatype].append(field)


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_is_used_by_a_field(datatype):
    assert datatype in field_datatypes


@pytest.mark.parametrize('register', registers)
def test_register_phase(register):
    assert registers[register].phase in phases


@pytest.mark.parametrize('field', fields)
def test_field_phase(field):
    assert fields[field].phase in phases


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_phase(datatype):
    assert datatypes[datatype].phase in phases
