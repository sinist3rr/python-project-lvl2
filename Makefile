install:
	@poetry install

test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

.PHONY: install test lint selfcheck check build
