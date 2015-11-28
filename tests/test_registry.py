import pytest

from data import registers, fields, registries, registry_registers


def test_registry_is_a_known_register():
    assert 'registry' in registers


@pytest.mark.parametrize('registry', registries)
def test_registry_key_matches_filename(registry):
    assert registries[registry].registry == registry


@pytest.mark.parametrize('registry', registries)
def test_registry_is_used_by_a_register(registry):
    assert registry in registry_registers
