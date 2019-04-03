.PHONY: test test_discovery test_alpha test_beta all

DISCOVERY_REGISTRIES:= $(wildcard data/discovery/registry/*.yaml)
DISCOVERY_REGISTERS:= $(wildcard data/discovery/register/*.yaml)
DISCOVERY_FIELDS:= $(wildcard data/discovery/field/*.yaml)
DISCOVERY_DATATYPES:= $(wildcard data/discovery/datatype/*.yaml)

ALPHA_REGISTRIES:= $(wildcard data/alpha/registry/*.yaml)
ALPHA_REGISTERS:= $(wildcard data/alpha/register/*.yaml)
ALPHA_FIELDS:= $(wildcard data/alpha/field/*.yaml)
ALPHA_DATATYPES:= $(wildcard data/alpha/datatype/*.yaml)

BETA_REGISTRIES:= $(wildcard data/beta/registry/*.yaml)
BETA_REGISTERS:= $(wildcard data/beta/register/*.yaml)
BETA_FIELDS:= $(wildcard data/beta/field/*.yaml)
BETA_DATATYPES:= $(wildcard data/beta/datatype/*.yaml)

all:	lint test
discovery:	lint test_discovery
alpha:	lint test_alpha
beta:	lint test_beta

lint:
	pipenv run flake8 bin tests

test_discovery:
	REGISTRY_ENV=discovery pipenv run py.test -v

test_alpha:
	REGISTRY_ENV=alpha pipenv run py.test -v

test_beta:
	REGISTRY_ENV=beta pipenv run py.test -v

test:	test_discovery test_alpha test_beta
