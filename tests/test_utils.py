import unittest

from app.utils import transform_phone, transform_name


class IndexText(unittest.TestCase):

    def test_transform_phone(self):
        phone = "677111999"
        transformed_phone = transform_phone(phone)
        self.assertEqual(transformed_phone, "+34677111999")

        # should not do anything
        phone = "+34666777888"
        transformed_phone = transform_phone(phone)
        self.assertEqual(transformed_phone, phone, "should not do anything!")

        self.assertRaises(Exception, transform_phone, "888")

    def test_transform_name(self):
        name = "Kevin"
        transformed_name = transform_name(name)
        self.assertEqual(transformed_name, "Fl Kevin")

        # should not do anything
        name = "Fl Rev Andreu"
        transformed_name = transform_name(name)
        self.assertEqual(transformed_name, name, "should not do anything!")


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
