import re
PREFIX = "Fl "
PHONE_COUNTRY_CODE = "+34"

regex_phone_with_country_code = r"^\+(?:[0-9]●?){6,14}[0-9]$"
regex_phone = r"^(?:[0-9]●?){9}$"


def transform_name(name):
    if name.startswith(PREFIX):
        return name
    return f"{PREFIX}{name}"


def transform_phone(phone):

    if re.fullmatch(regex_phone_with_country_code, phone):
        # print(f"'{phone}' is an fully qualified intl. number")
        # if PHONE_COUNTRY_CODE in phone:
        #     print('spanish number')
        return phone
    else:
        if not re.fullmatch(regex_phone, phone):
            raise f"Wrong input: The phone {phone} has less than 9 digits or is not a number!"
        return f"{PHONE_COUNTRY_CODE}{phone}"
