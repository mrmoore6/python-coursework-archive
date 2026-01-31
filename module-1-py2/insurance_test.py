import unittest
from insurance_quote import coverage_level,accidents,discounts

class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(accidents(40), 56.4)
    def test_two(self):
        self.assertEqual(discounts(40), 4)
    def test_three(self):
        with self.assertRaises(ValueError):
            coverage_level()

if __name__ == '__main__':
    unittest.main()
