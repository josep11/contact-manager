from os import path
import os
from random import randint
import re
import sys

from app.exceptions import InvalidNameException, WrongPhoneNumberException


PREFIX = "Fl "
PHONE_COUNTRY_CODE = "+34"

regex_phone_with_country_code = r"^\+(?:[0-9]●?){6,14}[0-9]$"
regex_phone = r"^(?:[0-9]●?){9}$"


def get_bundle_dir() -> str:
    # If it's bundled it will have _MEIPASS configured, else we default to this file
    # https://pyinstaller.org/en/v4.1/runtime-information.html
    # bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
    bundle_dir = os.getcwd()
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    return bundle_dir


def random_with_N_digits(n=9):
    range_start = 10**(n - 1)
    range_end = (10**n) - 1
    return randint(range_start, range_end)


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def substract_prefix_name(name):
    return name.replace(PREFIX, "")


def transform_name(name: str):
    if not name or name == "":
        raise InvalidNameException

    if name.startswith(PREFIX):
        return name
    return f"{PREFIX}{name}"


def transform_phone(phone: str):
    """will transform the phone to remove special characters like space, dash, etc and it will check that it is a phone number
    if there is no country code it will append the spanish (+34) by default

    Args:
        phone (str): the phone number (i.e. as copied from WhatsApp)

    Raises:
        WrongPhoneNumberException: the phone number is not ok

    Returns:
        str: the transformed phone number ready to save into Google Contacts
    """
    chars_to_remove = [" ", "(", ")", "-"]
    for char in chars_to_remove:
        phone = phone.replace(char, "")

    if re.fullmatch(regex_phone_with_country_code, phone):
        # print(f"'{phone}' is a fully qualified intl. number")
        return phone
    else:
        if not re.fullmatch(regex_phone, phone):
            raise WrongPhoneNumberException(
                f"Wrong input: The phone {phone} has less than 9 digits or is not a number!")
        return f"{PHONE_COUNTRY_CODE}{phone}"


# def inspect_bundle_dir():
#     import glob
#     bundle_dir = get_bundle_dir()
#     mylist = [f for f in glob.glob(f"{bundle_dir}/*")]

#     logger.info('\n'.join(mylist))

#     if os.path.exists(os.path.join(bundle_dir, ".env")):
#         logger.info('\n.env file exists')
#     else:
#         logger.error('\n.env file DOES NOT EXISTS')
