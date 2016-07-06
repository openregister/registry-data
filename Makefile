.PHONY: init test test_discovery test_alpha test_beta test_test all clean prod prod_alpha prod_beta prod_test

DISCOVERY_REGISTRIES:= $(wildcard data/discovery/registry/*.yaml)
DISCOVERY_REGISTERS:= $(wildcard data/discovery/register/*.yaml)
DISCOVERY_FIELDS:= $(wildcard data/discovery/field/*.yaml)
DISCOVERY_DATATYPES:= $(wildcard data/discovery/datatype/*.yaml)

DISCOVERY_PROD_DATA=\
	prod/discovery/registry.jsonl\
	prod/discovery/register.jsonl\
	prod/discovery/field.jsonl\
	prod/discovery/datatype.jsonl

ALPHA_REGISTRIES:= $(wildcard data/alpha/registry/*.yaml)
ALPHA_REGISTERS:= $(wildcard data/alpha/register/*.yaml)
ALPHA_FIELDS:= $(wildcard data/alpha/field/*.yaml)
ALPHA_DATATYPES:= $(wildcard data/alpha/datatype/*.yaml)

ALPHA_PROD_DATA=\
	prod/alpha/registry.jsonl\
	prod/alpha/register.jsonl\
	prod/alpha/field.jsonl\
	prod/alpha/datatype.jsonl

BETA_REGISTRIES:= $(wildcard data/beta/registry/*.yaml)
BETA_REGISTERS:= $(wildcard data/beta/register/*.yaml)
BETA_FIELDS:= $(wildcard data/beta/field/*.yaml)
BETA_DATATYPES:= $(wildcard data/beta/datatype/*.yaml)

BETA_PROD_DATA=\
	prod/beta/registry.jsonl\
	prod/beta/register.jsonl\
	prod/beta/field.jsonl\
	prod/beta/datatype.jsonl

TEST_REGISTRIES:= $(wildcard data/test/registry/*.yaml)
TEST_REGISTERS:= $(wildcard data/test/register/*.yaml)
TEST_FIELDS:= $(wildcard data/test/field/*.yaml)
TEST_DATATYPES:= $(wildcard data/test/datatype/*.yaml)

TEST_PROD_DATA=\
	prod/test/registry.jsonl\
	prod/test/register.jsonl\
	prod/test/field.jsonl\
	prod/test/datatype.jsonl

PROD_DATA=$(ALPHA_PROD_DATA) $(BETA_PROD_DATA) $(TEST_PROD_DATA)


all:	flake8 test prod
discovery:	flake8 test_discovery prod_discovery
alpha:	flake8 test_alpha prod_alpha
beta:	flake8 test_beta prod_beta
test:	flake8 test_test prod_test

prod_discovery:	$(DISCOVERY_PROD_DATA)

prod_alpha:	$(ALPHA_PROD_DATA)

prod_beta:	$(BETA_PROD_DATA)

prod_test: 	$(TEST_PROD_DATA)

prod:	prod_discovery prod_alpha prod_beta prod_test

prod/discovery/registry.jsonl:	bin/register_jsonl.py $(DISCOVERY_REGISTRIES)
	@mkdir -p prod/discovery
	bin/register_jsonl.py discovery registry > $@

prod/discovery/register.jsonl:	bin/register_jsonl.py $(DISCOVERY_REGISTERS)
	@mkdir -p prod/discovery
	bin/register_jsonl.py discovery register > $@

prod/discovery/field.jsonl:	bin/register_jsonl.py $(DISCOVERY_FIELDS)
	@mkdir -p prod/discovery
	bin/register_jsonl.py discovery field > $@

prod/discovery/datatype.jsonl:	bin/register_jsonl.py $(DISCOVERY_DATATYPES)
	@mkdir -p prod/discovery
	bin/register_jsonl.py discovery datatype > $@


prod/alpha/registry.jsonl:	bin/register_jsonl.py $(ALPHA_REGISTRIES)
	@mkdir -p prod/alpha
	bin/register_jsonl.py alpha registry > $@

prod/alpha/register.jsonl:	bin/register_jsonl.py $(ALPHA_REGISTERS)
	@mkdir -p prod/alpha
	bin/register_jsonl.py alpha register > $@

prod/alpha/field.jsonl:	bin/register_jsonl.py $(ALPHA_FIELDS)
	@mkdir -p prod/alpha
	bin/register_jsonl.py alpha field > $@

prod/alpha/datatype.jsonl:	bin/register_jsonl.py $(ALPHA_DATATYPES)
	@mkdir -p prod/alpha
	bin/register_jsonl.py alpha datatype > $@


prod/beta/registry.jsonl:	bin/register_jsonl.py $(BETA_REGISTRIES)
	@mkdir -p prod/beta
	bin/register_jsonl.py beta registry > $@

prod/beta/register.jsonl:	bin/register_jsonl.py $(BETA_REGISTERS)
	@mkdir -p prod/beta
	bin/register_jsonl.py beta register > $@

prod/beta/field.jsonl:	bin/register_jsonl.py $(BETA_FIELDS)
	@mkdir -p prod/beta
	bin/register_jsonl.py beta field > $@

prod/beta/datatype.jsonl:	bin/register_jsonl.py $(BETA_DATATYPES)
	@mkdir -p prod/beta
	bin/register_jsonl.py beta datatype > $@


prod/test/registry.jsonl:	bin/register_jsonl.py $(TEST_REGISTRIES)
	@mkdir -p prod/test
	bin/register_jsonl.py test registry > $@

prod/test/register.jsonl:	bin/register_jsonl.py $(TEST_REGISTERS)
	@mkdir -p prod/test
	bin/register_jsonl.py test register > $@

prod/test/field.jsonl:	bin/register_jsonl.py $(TEST_FIELDS)
	@mkdir -p prod/test
	bin/register_jsonl.py test field > $@

prod/test/datatype.jsonl:	bin/register_jsonl.py $(TEST_DATATYPES)
	@mkdir -p prod/test
	bin/register_jsonl.py test datatype > $@


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
