.PHONY: install shell format lint test sec

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
	@pytest -v

sec:
	@safety check
