
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

## Pip freeze dependencies into requirements.txt
pip/freeze:
	pip freeze > requirements.txt

## Run unit tests
test:
	python -m unittest discover