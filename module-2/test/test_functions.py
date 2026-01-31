#test
import unittest
from main import camper_age_input

class MyTestCase(unittest.TestCase):
    def test_months(self):
        self.assertEqual(54, camper_age_input.convert_to_months(7))


if __name__ == '__main__':
    unittest.main()
