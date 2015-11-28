import pytest

from data import registers, fields, datatypes, phases, field_datatypes


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_key_matches_filename(datatype):
    assert datatypes[datatype].datatype == datatype


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_keys_are_known_fields(datatype):
    for field in datatypes[datatype].keys:
        assert field in fields


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_datatypes_are_register_datatypes(datatype):
    for field in datatypes[datatype].keys:
        assert field in registers['datatype'].fields


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_text_trailing_characters(datatype):
    text = datatypes[datatype].text
    assert text == text.rstrip(' \n\r')


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_is_used_by_a_field(datatype):
    assert datatype in field_datatypes


@pytest.mark.parametrize('datatype', datatypes)
def test_datatype_phase(datatype):
    assert datatypes[datatype].phase in phases
