install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 page_loader tests/

format:
	poetry run isort --profile black page_loader tests
	poetry run black page_loader tests

bandit:
	poetry run bandit -r page_loader

safety:
	poetry run safety check

selfcheck:
	poetry check

check: selfcheck test format lint

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

.PHONY: install test lint selfcheck check build