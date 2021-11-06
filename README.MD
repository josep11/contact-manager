# Google Contacts Manager CLI

This is a command line utility to create/delete contacts used to integrate projects with ERP for freelancers.
It will create/delete the contact on the Authenticated Google Account if the contact with the same name does not exist.
When creating it will append a prefix "Fl" for the name to indicate Freelancer and the phone if there is no country code.

## Install for the first time

1. Download and have the 'client_secret.json' on the root folder. This can be downloaded from Google Cloud Platform > Contacts Sync App > Credentials
This will be useful for retriving the API Token via Oauth.
2. run `python install.py` to do OAuth and actually save the credentials to the .credentials folder.
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
create_contact -h # get help
```

```bash
./create_contact.py "AAAAAA TestContactName" "888888888"
# python create_contact.py "AAAAAA TestContactName" "888888888"
```

## Development

### Tests

```bash
# will find all tests named test*.py inside tests director
python -m unittest discover
```

## TODOs

- create a delete command to delete a contact by the name.
