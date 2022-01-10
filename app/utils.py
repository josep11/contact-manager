import re
import sys

from app.exceptions import WrongPhoneNumberException


PREFIX = "Fl "
PHONE_COUNTRY_CODE = "+34"

regex_phone_with_country_code = r"^\+(?:[0-9]●?){6,14}[0-9]$"
regex_phone = r"^(?:[0-9]●?){9}$"


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def transform_name(name):
    if name.startswith(PREFIX):
        return name
    return f"{PREFIX}{name}"


def transform_phone(phone):
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
