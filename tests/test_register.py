import re
import pytest

from data import registers, fields, phases, registries


def test_register_is_a_known_register():
    assert 'register' in registers


@pytest.mark.parametrize('register', registers)
def test_register_key_matches_filename(register):
    assert registers[register].register == register


@pytest.mark.parametrize('register', registers)
def test_register_primary_key_in_fields(register):
    assert register in registers[register].fields


@pytest.mark.parametrize('register', registers)
def test_register_keys_are_known_fields(register):
    for field in registers[register].keys:
        assert field in fields


@pytest.mark.parametrize('register', registers)
def test_register_fields_are_register_fields(register):
    for field in registers[register].keys:
        assert field in registers['register'].fields


@pytest.mark.parametrize('register', registers)
def test_register_text_trailing_characters(register):
    text = registers[register].text
    assert text == text.rstrip(' \n\r.')


@pytest.mark.parametrize('register', registers)
def test_register_text_double_spaces(register):
    text = registers[register].text
    assert text == re.sub(' +', ' ', text)


@pytest.mark.parametrize('register', registers)
def test_register_registry_is_known(register):
    assert registers[register].registry in registries


@pytest.mark.parametrize('register', registers)
def test_register_phase(register):
    assert registers[register].phase in phases


@pytest.mark.parametrize('register', registers)
def test_register_fields_are_known(register):
    item = registers[register]
    for field in item.fields:
        assert field in fields


@pytest.mark.parametrize('register', registers)
def test_register_fields_are_the_right_phase(register):
    item = registers[register]
    register_phase = phases.index(item.phase)
    for field in item.fields:
        field_phase = phases.index(fields[field].phase)
        assert field_phase >= register_phase
