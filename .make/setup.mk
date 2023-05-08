## Pip freeze dependencies
pip/freeze:
	pip freeze > requirements.txt

## Pip list outdated packages
pip/list-outdated:
	pip list --outdated

## Pip check for newer versions of dependencies
pip/check:
	pip-check -u -H

## Run pipreqs to save current direct dependencies into requirements.txt
pip/reqs:
	pipreqs --force

## Pip install dependencies from requirements.txt
pip/install:
	pip install -r requirements.txt

## Pip install dev dependencies
pip/install-dev:
	pip install -r requirements_dev.txt
