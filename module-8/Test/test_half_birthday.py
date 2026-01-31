import unittest
from more_fun_with_collections import half_birthday as birthday
from datetime import datetime
class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        test_date = datetime(2020,12,31)
        self.assertEqual("Your half b-day is 2021-07-01 12:00:00", birthday.half_birthday(test_date))


if __name__ == '__main__':
    unittest.main()
