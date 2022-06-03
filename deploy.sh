#!/bin/zsh

# Load .env file
[ -f .env ] && source .env

if [[ "$APP_NAME" == "" ]]; then
    echo error APP_NAME is not set in .env file && exit 1
fi

trash /Applications/$APP_NAME.app
cp -R dist/$APP_NAME.app /Applications/

# Now remove it from dist
trash dist/$APP_NAME.app