#!/bin/zsh
# aqui hace falta comprobar si tenemos instalado el
# pyinstall y si no es el caso instalarlo y preguntarle
# al usuario si quiere instalarlo
# Tambien tiene que leer el primer parametro que se
# encarga de añadir el nombre a la aplicacion

# pyinstaller --noconfirm --clean --onefile --noconsole --name $1 main.py

# -------------------------------- #
# -------- BEGIN CONFIG ---------- #
# -------------------------------- #
ENTRY_FILE=example.py
# TODO: move to .env
APP_NAME=ContactManager
BUNDLE_IDENTIFIER=com.josepalsina.contactmanager
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

python -m PyInstaller --windowed --noconfirm --clean --onefile --noconsole \
    --osx-bundle-identifier=$BUNDLE_IDENTIFIER \
    --name $APP_NAME \
    --exclude-module "$excluded_modules" \
    --debug=all \
    $ENTRY_FILE

    # --icon=paste.icns \

#    --add-binary edit_paste_app:edit_paste_app \

exit

echo build w debug options

pyinstaller --noconfirm --clean --onefile --noconsole \
    --osx-bundle-identifier=com.josepalsina.editpasteapp \
    --icon=paste.icns \
    --name EditPasteApp \
    --debug=imports \
    --log-level=DEBUG \
    entry.py