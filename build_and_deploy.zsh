#!/bin/zsh
# open -a "/Applications/$APP_NAME.app"
source .env

./build.zsh && ./deploy.zsh && source .env && terminal-notifier -message "deployed" \
-title "$APP_NAME" \
-execute "/Applications/$APP_NAME.app"