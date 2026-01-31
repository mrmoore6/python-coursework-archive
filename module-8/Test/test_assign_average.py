import unittest
from more_fun_with_collections import assign_average

class MyTestCase(unittest.TestCase):
    def test_average_A(self):
        self.assertEqual("You entered A", assign_average.switch_average('A'))

    def test_average_B(self):
        self.assertEqual("You entered B", assign_average.switch_average('B'))

    def test_average_C(self):
        self.assertEqual("You entered C", assign_average.switch_average('C'))

    def test_average_D(self):
        self.assertEqual("You entered D", assign_average.switch_average('D'))

    def test_average_E(self):
        self.assertEqual("You entered F", assign_average.switch_average('F'))

    def test_average_NON_KEY(self):
        self.assertEqual("This is grade doesn't exist.", assign_average.switch_average("Z"))



if __name__ == '__main__':
    unittest.main()
