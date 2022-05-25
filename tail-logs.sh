#!/bin/zsh

# Load .env file
[ -f .env ] && source .env

if [[ "$APP_NAME" == "" ]]; then
    echo error APP_NAME is not set in .env file && exit 1
fi

app_name_lower=$(echo "$APP_NAME" | python -c "print(open(0).read().lower())")

tail -f "~/Library/Logs/$APP_NAME/$app_name_lower.log"