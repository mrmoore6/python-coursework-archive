import unittest
from unittest.mock import patch
from fun_with_collections import basic_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [5, 5, 5])

    @patch('fun_with_collections.basic_list.get_input', return_value='bbb')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            basic_list.make_list()

    @patch('fun_with_collections.basic_list.get_input', return_value='60')
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            basic_list.make_list()

    @patch('fun_with_collections.basic_list.get_input', return_value='-1')
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):
            basic_list.make_list()



if __name__ == '__main__':
    unittest.main()
