.PHONY: install shell format lint test sec export configs run

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

configs:
	dynaconf -i src.config.settings list

run:
	@poetry run uvicorn src.main:create_app --factory --host 0.0.0.0 --port 8000 --reload

