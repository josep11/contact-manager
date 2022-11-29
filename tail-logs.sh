#!/bin/zsh

# Load .env file
[ -f .env ] && source .env

if [[ "$LOGS_DIRECTORY" == "" ]]; then
    echo error LOGS_DIRECTORY is not set in .env file && exit 1
fi

# app_name_lower=$(echo "$APP_NAME" | python -c "print(open(0).read().lower())")

tail -f "$LOGS_DIRECTORY"
