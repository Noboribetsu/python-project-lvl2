install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff

package-uninstall:
	python3 -m pip uninstall  dist/*.whl

gendiff:
	poetry run gendiff

.PHONY: gendiff
