# Google Contacts Sync

## Install for the first time

1. Download and have the 'client_secret.json' on the root folder. This can be downloaded from Google Cloud Platform > Contacts Sync App > Credentials
This will be useful for retriving the API Token via Oauth.
<!-- TODO:  -->
Maybe also when refresh tokens expires need to call step 2. for sure

2. run `python install.py` to do OAuth and actually save the credentials to the .credentials folder.

## Run

```bash
python create_contact.py "AB Default Contact Name" "888888888"
```

## Tests

## Hot to run tests

```bash
# will find all tests named test*.py inside tests director
python -m unittest discover
```
