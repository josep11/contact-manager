# Google Contacts Creator CLI

This is a contacts creator command line interface used to integrate projects with ERP for freelancers.
It will create the contact on the Authenticated Google Account if the contact with the same name does not exist.
It will append a prefix "Fl" for the name to indicate Freelancer and the phone if there is no country code.

## Install for the first time

1. Download and have the 'client_secret.json' on the root folder. This can be downloaded from Google Cloud Platform > Contacts Sync App > Credentials
This will be useful for retriving the API Token via Oauth.
2. run `python install.py` to do OAuth and actually save the credentials to the .credentials folder.
3. `cp .env.example .env` and set environment variables apropiately
4. [Optional] See [install globally](#install-globally) section

### Install Globally

Copy the following into ~/.bash_profile, ~/.profile or equivalent to install it as a system wide command:

```bash
###### Contacts Creator #######
function create_contact(){
    CONTACTS_CREATOR_ROOTDIR=/path/to/where/the/project/is/installed
    cd "$CONTACTS_CREATOR_ROOTDIR";
    ./create_contact.py "$@"
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
