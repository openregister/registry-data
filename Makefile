.PHONY: init test test_alpha all clean prod prod_alpha

ALPHA_REGISTRIES:= $(wildcard data/alpha/registry/*.yaml)
ALPHA_REGISTERS:= $(wildcard data/alpha/register/*.yaml)
ALPHA_FIELDS:= $(wildcard data/alpha/field/*.yaml)
ALPHA_DATATYPES:= $(wildcard data/alpha/datatype/*.yaml)

ALPHA_PROD_DATA=\
	prod/alpha/registry.jsonl\
	prod/alpha/register.jsonl\
	prod/alpha/field.jsonl\
	prod/alpha/datatype.jsonl

PROD_DATA=$(ALPHA_PROD_DATA)

all:	flake8 test prod

prod_alpha:	$(ALPHA_PROD_DATA)

prod:	prod_alpha

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

flake8:
	flake8 bin tests

test_alpha:
	REGISTRY_ENV=alpha py.test -v

test:	test_alpha

clean:
	find . -name "*.pyc" | xargs rm -f
	find . -name "__pycache__" | xargs rm -rf
	rm -f $(PROD_DATA)

init:
	pip3 install --upgrade -r requirements.txt
