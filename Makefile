
default: help

## Help
help:
	@printf "Available targets:\n\n"
	@awk '/^[a-zA-Z\-\_0-9%:\\]+/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
		helpCommand = $$1; \
		helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
	gsub("\\\\", "", helpCommand); \
	gsub(":+$$", "", helpCommand); \
		printf "  \x1b[32;01m%-35s\x1b[0m %s\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST) | sort -u
	@printf "\n"

## Lists all targets defined in the makefile.
list:
	@$(MAKE) -pRrn : -f $(MAKEFILE_LIST) 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | command grep -v -e '^[^[:alnum:]]' -e '^$@$$command ' | sort

include .make/*.mk

## Tail the logs
logs-tail:
	@sh ./tail-logs.sh

## Tail the logs
tail-logs: logs-tail

## Build
build:
	$(shell ./build.zsh)

## Build and run
build-and-run:
	@echo ./build_and_run.zsh
# $(shell ./build_and_run.zsh)

## Build and deploy
build-and-deploy:
	@echo ./build_and_deploy.zsh

## Cleans up already merged branches
git/clean:
	git fetch origin --prune

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

## Run unit tests
test:
	pytest -q

_check-requirement:
	@${COMMAND} --version >/dev/null 2>&1 || (echo "ERROR: ${COMMAND} is required."; exit 1)

## Ensures that the the requirements for dev are installed
.PHONY: _ensure-requirements-dev
_ensure-requirements-dev:
	@pytest --version >/dev/null 2>&1 || (echo "ERROR: pytest is required. Please run make pip/install-dev"; exit 1)

