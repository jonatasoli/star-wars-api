.PHONY: install shell format lint test sec export

install:
	@poetry install

shell:
	@poetry shell

format:
	@isort .
	@blue .

lint:
	@blue . --check
	@isort . --check
	@prospector --with-tool pep257 --doc-warning

test:
	@pytest -s -m 'not api'

sec:
	@safety check

export:
	@poetry export -f requirements.txt --output requirements.txt
