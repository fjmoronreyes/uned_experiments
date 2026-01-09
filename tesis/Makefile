SHELL := /bin/bash
PYTHON := /usr/bin/python3.12

.PHONY: setup install kernel check shell

setup:
	poetry config virtualenvs.in-project true --local
	poetry config virtualenvs.create true --local
	poetry env use $(PYTHON)

install:
	poetry install
	poetry add numpy pandas scikit-learn python-dotenv openai
	poetry add --group dev jupyter ipykernel || poetry add --dev jupyter ipykernel

kernel:
	poetry run python -m ipykernel install --user --name tesis --display-name "Python (tesis)"

check:
	poetry run python -c "import numpy, sklearn, openai; print('ok')"

shell:
	poetry shell
	@echo "Activated poetry shell. To exit, type 'exit'."