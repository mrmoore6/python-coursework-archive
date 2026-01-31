import unittest
from Input_Functions import user, user_avg
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    def test_one(self):
        user(-4)
        self.assertEqual(user(),"Enter Correct Input")


if __name__ == '__main__':
    unittest.main()
