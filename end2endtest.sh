
# test contact create

# spreadsheet id test
# export SPREADSHEET_ID=1TtgSjRT6H720g6DZo8_mxyISCL94fUQ6-seLfJKgJco

# text_ok_create="Created contact"
# text_ok_create_2="cells updated"

export ENV=test

SLEEP_SECONDS=60


rand=$(echo $RANDOM)
rand_contact_name="AAAAAA TestContactName $rand"

./create_contact.py "$rand_contact_name" "888888888"

echo; echo "waiting $SLEEP_SECONDS seconds before deleting"; echo

sleep "$SLEEP_SECONDS"

./delete_contact.py "$rand_contact_name"

# TODO: check and set the exit code depending on result
# echo $?

##########
# OK output example create
##########

# Created directory: /tmp/Examens_Treballs/aaaaa delete prova
# About to create Fl aaaaa delete prova with phone +34999999999
# Created contact Fl aaaaa delete prova with phone +34999999999
# 2 contacts retrieved from spreadsheet
# 3 cells updated.
