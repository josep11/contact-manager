# Recreate virtualenv

pyenv version
cat .python-version

## Upgrade

brew update
brew upgrade pyenv

pyenv install --list | grep 3.12
pyenv install 3.12.8

### Create a new venv

pyenv virtualenv 3.12.8 py3.12.8-contact-manager
pyenv virtualenvs

pyenv activate py3.12.8-contact-manager
pyenv local py3.12.8-contact-manager

python --version

## Clean up old

pyenv uninstall py3.10.4-contact-manager
