#!/bin/zsh

./build.zsh

echo after build

# Load .env file
[ -f .env ] && source .env

if [[ "$APP_NAME" == "" ]]; then
    echo error APP_NAME is not set in .env file && exit 1
fi

echo opening compiled app
open "dist/$APP_NAME.app"