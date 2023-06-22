.PHONY: dep
dep:
	pip install poetry
	poetry install

.PHONY: run
run:
	poetry run python -V
