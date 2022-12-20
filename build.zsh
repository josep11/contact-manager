#!/bin/zsh
# aqui hace falta comprobar si tenemos instalado el
# pyinstall y si no es el caso instalarlo y preguntarle
# al usuario si quiere instalarlo
# Tambien tiene que leer el primer parametro que se
# encarga de añadir el nombre a la aplicacion

# pyinstaller --noconfirm --clean --onefile --noconsole --name $1 main.py

# Load .env file
[ -f .env ] && source .env

if [[ "$APP_NAME" == "" ]]; then
    echo error APP_NAME is not set in .env file && exit 1
fi

# -------------------------------- #
# -------- BEGIN CONFIG ---------- #
# -------------------------------- #
# PRODUCTION_BUILD=0
ENTRY_FILE=contact_manager_gui.py
# -------------------------------- #
# -------- END CONFIG ---------- #
# -------------------------------- #


echo APP VERSION $(cat app/__init__.py | grep version | awk '{split($0,a,"="); print a[2]}' | sed "s/'//g")
python -V
echo

# If using python 3.10.x use "--exclude-module _bootlocale"
PYTHON_VERSION=$(python -V)
excluded_modules="_dummy"
if [[ "$PYTHON_VERSION" == *"3.10"* ]]; then
    excluded_modules+=" _bootlocale"
fi

# trying to set the python library path for pyinstaller to know where it is in order to bundle it
export DYLD_LIBRARY_PATH=$(which python)

python -m PyInstaller --noconfirm --log-level=WARN \
    --clean --onefile -w \
    --osx-bundle-identifier=$BUNDLE_IDENTIFIER \
    --name $APP_NAME \
    --icon=contact-manager.icns \
    --exclude-module "$excluded_modules" \
    --add-data ".env:." \
    --add-data "client_secret.json:." \
    --debug=imports \
    $ENTRY_FILE
    
    # --add-data ".credentials:." \
    # 
    # -w \
    # --icon=paste.icns \

#    --add-binary edit_paste_app:edit_paste_app \

exit
