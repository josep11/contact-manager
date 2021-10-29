import argparse

from app.create_contact import main

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str,
                        help="the name of the contact to create")
    parser.add_argument("phone", type=str,
                        help="the phone of the contact to create")
    args = parser.parse_args()
except ImportError:
    args = None

if __name__ == "__main__":
    name = args.name
    phone = args.phone
    main(name, phone)
