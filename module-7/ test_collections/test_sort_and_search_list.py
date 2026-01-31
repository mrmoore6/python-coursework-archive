import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_list

class MyTestCase(unittest.TestCase):
        def test_sorted_list(self):
            self.assertListEqual([1,2,3], sort_and_search_list.sort_list([3,2,1]))
        def test_search_list(self):
            self.assertEqual(2, sort_and_search_list.search_list([3,2,1]))
       #enter 1 for index of 2




if __name__ == '__main__':
    unittest.main()
