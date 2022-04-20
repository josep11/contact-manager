# Google Contacts Manager CLI

This is a command line utility to create/delete contacts used to integrate projects with ERP for freelancers.
It will create/delete the contact on the Authenticated Google Account if the contact with the same name does not exist.
When creating it will append a prefix "Fl" for the name to indicate Freelancer and the phone if there is no country code.

## Install for the first time

1. Download and have the 'client_secret.json' at the root folder. This can be downloaded from Google Cloud Platform > Contacts Sync App > Credentials
This will be useful for retriving the API Token via Oauth.
2. Install dependencies: `pip install -r requirements.txt`
> If it's not working you may need to install the private dependencies like so: `pip install git+https://github.com/josep11/google-oauth-wrapper.git`
3. (optional) run `python install.py` to do OAuth (make sure to check the permissions) and then the script will save the credentials to the .credentials folder.
4. `cp .env.example .env` and set environment variables apropiately
5. [Optional] See [install globally](#install-globally) section

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

<!-- ```bash
./create_contact.py "AAAAAA TestContactName" "888888888"
# python create_contact.py "AAAAAA TestContactName" "888888888"
``` -->

## Development

### Tests

```bash
# will find all tests named test*.py inside tests director
python -m unittest discover
```
