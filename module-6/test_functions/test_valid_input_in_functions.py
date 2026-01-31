import unittest
from more_functions import validate_input_in_functions as valid_function

class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Math: 0%", valid_function.score_input("Math"))

    def test_score_input_test_valid(self):
        self.assertEqual("History: 85%", valid_function.score_input("History",85))

    def test_score_input_test_below_range(self):
        self.assertEqual('Invalid test score, try again!', valid_function.score_input("Geometry",-5))

    def test_score_input_test_above_range(self):
        self.assertEqual('Invalid test score, try again!', valid_function.score_input("Science", 299))

    def test_score_input_test_non_numeric(self):
        with self.assertRaises(TypeError):
            valid_function.score_input("P.E", "Alpha")

    def test_score_input_test_invalid_message(self):
        self.assertEqual('try again!', valid_function.score_input("Science", 299,'try again!'))


if __name__ == '__main__':
    unittest.main()
