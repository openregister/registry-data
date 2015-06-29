REGISTER_URL=http://register.openregister.org
DATATYPE_URL=http://register.openregister.org

register:
	bin/post_to_register.py --d data/Register --r ${REGISTER_URL}

datatype:
	bin/post_to_register.py --d data/Datatype --r ${DATATYPE_URL}

clean:
	find . -name "*.pyc" | xargs rm -f
	find . -name "__pycache__" | xargs rm -rf

init:
	pip3 install -r requirements.txt
