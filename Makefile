.PHONY: init test test_discovery test_alpha test_beta test_test all clean prod prod_alpha prod_beta prod_test

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

TEST_REGISTRIES:= $(wildcard data/test/registry/*.yaml)
TEST_REGISTERS:= $(wildcard data/test/register/*.yaml)
TEST_FIELDS:= $(wildcard data/test/field/*.yaml)
TEST_DATATYPES:= $(wildcard data/test/datatype/*.yaml)

all:	flake8 test prod
discovery:	flake8 test_discovery prod_discovery
alpha:	flake8 test_alpha prod_alpha
beta:	flake8 test_beta prod_beta
test:	flake8 test_test prod_test

flake8:
	flake8 bin tests

test_discovery:
	REGISTRY_ENV=discovery py.test -v

test_alpha:
	REGISTRY_ENV=alpha py.test -v

test_beta:
	REGISTRY_ENV=beta py.test -v

test_test:
	REGISTRY_ENV=test py.test -v

test:	test_discovery test_alpha test_beta test_test

clean:
	find . -name "*.pyc" | xargs rm -f
	find . -name "__pycache__" | xargs rm -rf
	rm -f $(PROD_DATA)

init:
	pip3 install --upgrade -r requirements.txt
