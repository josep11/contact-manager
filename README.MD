# Google Contacts Manager

This is a command line and GUI utility to create/delete contacts used to integrate projects with ERP for freelancers.
It will create/delete the contact on the Authenticated Google Account if the contact with the same name does not exist.
When creating it will append a prefix "Fl" for the name to indicate Freelancer and the phone if there is no country code.

## Icons

[Nice page with free icons](https://iconarchive.com/)

## Create Virtualenv and install deps

If we are going to build we need to install the python version like this:

```bash
env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.10.4
```

Creating python environment with pyenv:

```bash
pyenv virtualenv 3.10.4 py3.10.4-contact-manager
```

Activate it from this directory:

```bash
pyenv local py3.10.4-contact-manager
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If it's not working you may need to install the private dependencies like so:

```bash
pip install git+https://github.com/josep11/google-oauth-wrapper.git
```

## Configure for the first time

1. Download and have the 'client_secret.json' at the root folder. This can be downloaded from Google Cloud Platform > Contacts Sync App > Credentials
This will be useful for retriving the API Token via Oauth.
2. (optional) run `python install.py` to do OAuth (make sure to check the permissions) and then the script will save the credentials to the .credentials folder.
3. `cp .env.example .env` and set environment variables apropiately
4. [Optional] See [install globally](#install-globally) section

### Install Globally

Copy the following into ~/.bash_profile, ~/.profile or equivalent to install it as a system wide command:

```bash
###### Contacts Manager #######
export CONTACTS_MANAGER_ROOTDIR=/path/to/where/the/project/is/installed

function create_contact(){
    cd "$CONTACTS_MANAGER_ROOTDIR";
    ./create_contact.py "$@"
    cd - 1>/dev/null
}

function delete_contact(){
    cd "$CONTACTS_MANAGER_ROOTDIR";
    ./delete_contact.py "$@"
    cd - 1>/dev/null
}
```

## Run

```bash
create_contact "full name" "phone number"
delete_contact "full name"

create_contact -h
```

To run an end to end test:

```bash
./end2endtest.sh
```

If running create_contact or delete_contact with ENV=test it will load:

1) the `.env` file
2) the `.env.test` file. Overriding the values.

## Development

### Tests

```bash
# will find all tests named test*.py inside tests director
python -m unittest discover
```

## Future lines

[Nice tutorial to build executables with pyinstaller](https://www.youtube.com/watch?v=3xuN9JQ7j1Q&ab_channel=CodingEntrepreneurs)

### Build and run the built version

Make sure that the .env file includes all variables like in `.env.example`.
Make sure that the shebang on all the `./*.sh` is the same as your default shell. To get it: `echo $SHELL`. Then

```bash
./build.sh && source .env && open dist/$APP_NAME.app
```

## Deployment

Warning: before deploying make sure that you delete the previous build file from /Applications as I found there may be traces that will cause conflicts with newer builds.

### Before Deploy

#### Remove unused imports

Either of the two:

```bash
autoflake -i --remove-all-unused-imports *.py **/**.py
python -m autoflake -i --remove-all-unused-imports *.py **/**.py
```

### Deploy

```bash
./deploy.sh
```

### Build and Deploy

```bash
./build_and_deploy.sh
```
