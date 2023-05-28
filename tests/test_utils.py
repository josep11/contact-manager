import unittest

from app.utils import open_browser, transform_phone, transform_name, substract_prefix_name


class IndexText(unittest.TestCase):

    def test_transform_phone(self):
        phone = "623 00 28 92"
        transformed_phone = transform_phone(phone)
        self.assertEqual(transformed_phone, "+34623002892")

        phone = "677111999"
        transformed_phone = transform_phone(phone)
        self.assertEqual(transformed_phone, "+34677111999")

        # should not do anything
        phone = "+34666777888"
        transformed_phone = transform_phone(phone)
        self.assertEqual(transformed_phone, phone, "should not do anything!")

        phone = "+1 (850) 993-1568"
        transformed_phone = transform_phone(phone)
        self.assertEqual(transformed_phone, "+18509931568")

        self.assertRaises(BaseException, transform_phone, "888")

    def test_transform_name(self):
        name = "Kevin"
        transformed_name = transform_name(name)
        self.assertEqual(transformed_name, "Fl Kevin")

        # should not do anything
        name = "Fl Rev Andreu"
        transformed_name = transform_name(name)
        self.assertEqual(transformed_name, name, "should not do anything!")

        name = "Fl Javi"
        name_without_prefix = "Javi"
        self.assertEqual(substract_prefix_name(name), name_without_prefix)

    def test_open_browser(self):
        url = "https://docs.google.com/"
        open_browser(url)


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
