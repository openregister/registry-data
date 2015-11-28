REGISTER_REGISTER=http://register.openregister.org
FIELD_REGISTER=http://register.openregister.org
DATATYPE_REGISTER=http://datatype.openregister.org

.PHONY: init test all clean prod

REGISTERS:= $(wildcard data/register/*.yaml)
FIELDS:= $(wildcard data/field/*.yaml)
DATATYPES:= $(wildcard data/datatype/*.yaml)

PROD_DATA=\
	prod/register.jsonl\
	prod/field.jsonl\
	prod/datatype.jsonl

all:	flake8 test prod

prod:	$(PROD_DATA)

prod/register.jsonl:	bin/register_jsonl.py $(REGISTERS)
	@mkdir -p prod
	bin/register_jsonl.py register > $@

prod/field.jsonl:	bin/register_jsonl.py $(FIELDS)
	@mkdir -p prod
	bin/register_jsonl.py field > $@

prod/datatype.jsonl:	bin/register_jsonl.py $(DATATYPES)
	@mkdir -p prod
	bin/register_jsonl.py datatype > $@

flake8:
	flake8 bin tests

test:
	py.test -v

clean:
	find . -name "*.pyc" | xargs rm -f
	find . -name "__pycache__" | xargs rm -rf
	rm -f $(PROD_DATA)

init:
	pip3 install --upgrade -r requirements.txt
