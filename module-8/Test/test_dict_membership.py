import unittest
from more_fun_with_collections import dict_membership

class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        test_dict = {"A:50","B:60","C:40","D:60"}
        self.assertEqual("{}, {}".format(True,test_dict), dict_membership.in_dict("50", test_dict))
    def test_in_dict_false(self):
        test_dict = {"A:50", "B:60", "C:40", "D:60"}
        self.assertEqual("{}, {}".format(False,test_dict),dict_membership.in_dict('20', test_dict))


if __name__ == '__main__':
    unittest.main()
