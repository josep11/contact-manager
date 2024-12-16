## List pyenv versions
pyenv/versions:
	pyenv versions

## List pyenv versions (possible to install)
pyenv/install-list:
	pyenv install --list

## Install a new python version through pyenv. make pyenv/install VERSION=3.12.2
pyenv/install:
	pyenv install ${VERSION}

## Create a virtual environment for a project. make pyenv-virtualenv/create VERSION=3.12.2 PROJECT_NAME=my-project-name
pyenv-virtualenv/create:
	pyenv virtualenv ${VERSION} py${VERSION}-${PROJECT_NAME}

## Activate a virtual environment locally. make pyenv-virtualenv/activate VENV_NAME=py3.12.2-my-project-name
pyenv-virtualenv/activate:
	pyenv local ${VENV_NAME}

## Pip freeze dependencies
pip/freeze:
	pip freeze > requirements.txt

## Pip check for newer versions of dependencies
pip/check:
	pip-check -u -H

## Pip list outdated packages
pip/list-outdated:
	pip list --outdated

## Run pipreqs to save current direct dependencies into requirements.txt
pip/reqs:
	pipreqs --force

## Pip install dependencies from requirements.txt
pip/install: pip/install-custom
	pip install -r requirements.txt

## Pip install dev dependencies
pip/install-dev: pip/install-custom
	pip install -r requirements_dev.txt

## Pip remove a dependency: make pip/remove PACKAGE="autoflake autopep8 black"
pip/remove:
	pip uninstall -y ${PACKAGE}
	make pip/freeze

## Installs project-specific dependencies that might not be in requirements* files
pip/install-custom:
	pip install git+https://github.com/josep11/google-oauth-wrapper.git