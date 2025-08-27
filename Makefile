.PHONY: setup format lint type test docs

setup:
pip install -e .[all]

format:
black src tests

lint:
ruff check src tests

type:
mypy src

test:
pytest

docs:
mkdocs build

