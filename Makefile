
default: help

include .make/*.mk

## Tail the logs
logs-tail:
	@sh ./tail-logs.sh

## Tail the logs
tail-logs: logs-tail

## Build
build:
	./build.zsh

## Build and run
build-and-run:
	./build_and_run.zsh

## Build and deploy
build-and-deploy:
	./build_and_deploy.zsh

## Cleans up already merged branches
git/clean:
	git fetch origin --prune

## Run unit tests
test:
	make _ensure-requirements-dev
	pytest -q

## Ensures that the the requirements for dev are installed
_ensure-requirements-dev:
	@pytest --version >/dev/null 2>&1 || (echo "ERROR: pytest is required. Please run make pip/install-dev"; exit 1)

.PHONY: _ensure-requirements-dev
