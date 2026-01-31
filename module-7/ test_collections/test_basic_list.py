import unittest
from unittest.mock import patch
from fun_with_collections import basic_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='55')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [55, 55, 55])




if __name__ == '__main__':
    unittest.main()

