.PHONY: init test test_alpha test_beta all clean prod prod_alpha prod_beta

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

PROD_DATA=$(ALPHA_PROD_DATA) $(BETA_PROD_DATA)

all:	flake8 test prod
alpha:	flake8 test_alpha prod_alpha
beta:	flake8 test_beta prod_beta

prod_alpha:	$(ALPHA_PROD_DATA)

prod_beta:	$(BETA_PROD_DATA)

prod:	prod_alpha prod_beta

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

flake8:
	flake8 bin tests

test_alpha:
	REGISTRY_ENV=alpha py.test -v

test_beta:
	REGISTRY_ENV=beta py.test -v

test:	test_alpha test_beta

clean:
	find . -name "*.pyc" | xargs rm -f
	find . -name "__pycache__" | xargs rm -rf
	rm -f $(PROD_DATA)

init:
	pip3 install --upgrade -r requirements.txt
