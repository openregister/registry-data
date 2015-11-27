REGISTER_REGISTER=http://register.openregister.org
FIELD_REGISTER=http://register.openregister.org
DATATYPE_REGISTER=http://datatype.openregister.org

.PHONY: init test all clean prod

PROD_DATA=\
	prod/register.jsonl\
	prod/field.jsonl\
	prod/datatype.jsonl

all:	prod

prod:	$(PROD_DATA)

prod/register.jsonl:	bin/register_jsonl.py
	bin/register_jsonl.py register > $@

prod/field.jsonl:	bin/register_jsonl.py
	bin/register_jsonl.py field > $@

prod/datatype.jsonl:	bin/register_jsonl.py
	bin/register_jsonl.py datatype > $@

clean:
	find . -name "*.pyc" | xargs rm -f
	find . -name "__pycache__" | xargs rm -rf
	rm -f $(PROD_DATA)

init:
	pip3 install --upgrade -r requirements.txt
