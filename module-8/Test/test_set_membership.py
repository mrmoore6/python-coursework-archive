import unittest
from more_fun_with_collections import set_membership


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        set = {1,2,3,4,5,6,6,7564,324,4224}
        self.assertEqual(True,set_membership.in_set(set,4))
    def test_in_set_false(self):
        set = {1,23,3,3434,3,2,3,2,'3'}
        self.assertEqual(False,set_membership.in_set(set,5))

if __name__ == '__main__':

    unittest.main()
