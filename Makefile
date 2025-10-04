.PHONY: help install install-dev test lint format type-check quality clean build

help:  ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

install:  ## Install production dependencies
	pip install -e .

install-dev:  ## Install development dependencies
	pip install -e ".[dev]"
	pre-commit install

test:  ## Run tests with coverage
	pytest

test-fast:  ## Run tests without coverage
	pytest --no-cov

lint:  ## Run linting checks
	ruff check src tests

lint-fix:  ## Run linting with auto-fix
	ruff check --fix src tests

format:  ## Format code with ruff
	ruff format src tests

format-check:  ## Check code formatting
	ruff format --check src tests

type-check:  ## Run type checking with mypy
	mypy src

complexity:  ## Check code complexity
	@echo "Cyclomatic Complexity:"
	@radon cc src --min B --total-average
	@echo "\nMaintainability Index:"
	@radon mi src --min B

docstring-coverage:  ## Check docstring coverage
	interrogate -vv src

quality: lint format-check type-check complexity docstring-coverage test  ## Run all quality checks

pre-commit:  ## Run pre-commit hooks on all files
	pre-commit run --all-files

clean:  ## Clean build artifacts and cache
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:  ## Build distribution packages
	python -m build

publish-test:  ## Publish to Test PyPI
	python -m twine upload --repository testpypi dist/*

publish:  ## Publish to PyPI
	python -m twine upload dist/*
