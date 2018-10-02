# Top-level control of the building/installation/cleaning of various targets

# python virtual environment
VIRTUALENV_DIR := .venv
ACTIVATE := $(VIRTUALENV_DIR)/bin/activate

.PHONY: default run_venv clean_pyc clean style venv spec

default: run_venv

venv: $(ACTIVATE)
$(ACTIVATE): requirements.txt
	@echo "Updating virtualenv dependencies in: $(VIRTUALENV_DIR)..."
	@test -d $(VIRTUALENV_DIR) || virtualenv $(VIRTUALENV_DIR)
	@. $(ACTIVATE); pip install -Ur requirements.txt
	@touch $(ACTIVATE)

run_venv: venv
	@echo "Virtualenv running (on port 8080)..."
	$(VIRTUALENV_DIR)/bin/python main.py

build:
	@docker build -t dls_challenge .

run_container: build
	@docker run -d -p 8080:8080 dls_challenge

clean_pyc:
	@-find . -name '*.py[co]' -exec rm {} \;

clean: clean_pyc
	@echo "Removing virtual environment files"
	@rm -rf $(VIRTUALENV_DIR)

test: venv
	@. $(ACTIVATE); echo "TODO: Add some tests.  Maybe look at tox or pyunit"

style: venv
	@. $(ACTIVATE); flake8 --exclude=.venv .

# due to a bug with flaskswagger, going to write spec out to an output dir
# and then redirect that to the screen. Otherwise it prints the spec twice
spec: venv
	@. $(ACTIVATE); flaskswagger main:app --out-dir . && cat swagger.json && echo && rm swagger.json
