import unittest
from more_functions import inner_functions_assignment as in_functon

class MyTestCase(unittest.TestCase):
    def test_measurements_rectangle(self):
        self.assertEqual(in_functon.measurements([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(in_functon.measurements([3.5]), "Perimeter = 14.0 Area = 12.25")

    def test_measurements_no_value(self):
        self.assertEqual(in_functon.measurements([]), "Input 1 or 2 measurements!")

    def test_measurements_extra_value(self):
        self.assertEqual(in_functon.measurements([3.5, 2, 3]), "Input 1 or 2 measurements!")


if __name__ == '__main__':
    unittest.main()
