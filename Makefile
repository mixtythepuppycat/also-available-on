venv/bin/python:
	virtualenv venv
	venv/bin/pip install -r requirements.txt

install: requirements.txt
	virtualenv venv
	venv/bin/pip install -r requirements.txt

.PHONY: run
run: venv/bin/python
	 venv/bin/python bot.py