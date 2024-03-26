SRC_FOLDER=src
SRC_TEST=tests
PYTHON=python3
PYDOC=pydoc3
PYTEST=pytest
PIP=pip3
APP_ENTRYPOINT=$(SRC_FOLDER)/main.py

help: ## Prints these help pages
	$(info Commands available:)
	$(info )
	@grep '^[[:alnum:]_-]*:.* ##' $(MAKEFILE_LIST) \
		| sort | awk 'BEGIN {FS=":.* ## "}; {printf "%-25s %s\n", $$1, $$2};'

run: ## Run the code
	@$(PYTHON) $(APP_ENTRYPOINT)

test: ## Run tests in the tests/ folder. Outputs HTML results in folder htmlcov/
	$(PYTEST) -vv --cov=src --cov-report html
	$(PYTEST) -vv --cov=src

doc: ## Output pdoc HTML code documentation into folder docs/
	rm -rf ./docs
	pdoc $(SRC_FOLDER)/* -o docs --docformat google

clean: ## Remove all automatically generated files and folders
	rm -rf docs/
	rm -rf htmlcov
	rm -rf .pytest_cache
	rm .coverage

install-deps: ## Install all required pip packages
	pip3 install -r requirements.txt