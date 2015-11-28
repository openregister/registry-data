import pytest

from data import registries, registry_registers


@pytest.mark.parametrize('registry', registries)
def test_registry_key_matches_filename(registry):
    assert registries[registry].registry == registry


@pytest.mark.parametrize('registry', registries)
def test_registry_is_used_by_a_register(registry):
    assert registry in registry_registers
