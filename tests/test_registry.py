import pytest

from data import registers, fields, registries, \
    registry_registers


@pytest.mark.xfail(reason="registry register not currently supported",
                   strict=True)
def test_registry_is_a_known_register():
    assert 'registry' in registers


@pytest.mark.parametrize('registry', registries)
def test_registry_key_matches_filename(registry):
    assert registries[registry].registry == registry


@pytest.mark.parametrize('registry', registries)
def test_registry_is_used_by_a_register(registry):
    assert registry in registry_registers


@pytest.mark.parametrize('registry', registries)
def test_registry_keys_are_known_fields(registry):
    for field in registries[registry].keys:
        assert field in fields


@pytest.mark.xfail(reason="registry register not currently supported",
                   strict=True)
@pytest.mark.parametrize('registry', registries)
def test_registry_registries_are_register_registries(registry):
    for field in registries[registry].keys:
        assert field in registers['registry'].fields
