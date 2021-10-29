# Google Contacts Creator CLI

This is a contacts creator command line interface used to integrate projects with ERP for freelancers.
It will create the contact on the Authenticated Google Account if the contact with the same name does not exist.
It will append a prefix "Fl" for the name to indicate Freelancer and the phone if there is no country code.

## Install for the first time

1. Download and have the 'client_secret.json' on the root folder. This can be downloaded from Google Cloud Platform > Contacts Sync App > Credentials
This will be useful for retriving the API Token via Oauth.
2. run `python app/install.py` to do OAuth and actually save the credentials to the .credentials folder.

## Run

```bash
python main.py "AB Default Contact Name" "888888888"
```

## Tests

```bash
# will find all tests named test*.py inside tests director
python -m unittest discover
```
