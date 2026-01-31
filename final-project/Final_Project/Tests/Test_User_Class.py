import unittest
from Final_Project.Classes.User_Class import User

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_user = User("Mike","Moore",20,190.5,5,10)

    def tearDown(self):
        del self.test_user

    def test_valid_f_name(self):
        self.assertEqual(self.test_user.f_name, "Mike")

    def test_valid_l_name(self):
        self.assertEqual(self.test_user.l_name, "Moore")

    def test_valid_age(self):
        self.assertEqual(self.test_user.age, 20)

    def test_valid_weight(self):
        self.assertEqual(self.test_user.weight, 190.5)

    def test_valid_height_feet(self):
        self.assertEqual(self.test_user.height_feet, 5)

    def test_valid_height_inches(self):
        self.assertEqual(self.test_user.height_inches, 10)



    def test_invalid_f_name(self):
        with self.assertRaises(TypeError):
            test_user = User("M1223", "Moore", 22, 190.5,5,10)

    def test_invalid_l_name(self):
        with self.assertRaises(TypeError):
            test_user = User("Mike", "M12e2", 22, 190.5,5,10)

    def test_invalid_age_Alpha(self):
        with self.assertRaises(ValueError):
            test_user = User("Mike", "Moore", '22', 190.5,5,10)

    def test_invalid_age_MAX(self):
        with self.assertRaises(ValueError):
            test_user = User("Mike", "Moore", 220, 190.5,5,10)

    def test_invalid_age_MIN(self):
        with self.assertRaises(ValueError):
            test_user = User("Mike", "Moore", -3, 190.5,5,10)

    def test_invalid_weight_Alpha(self):
        with self.assertRaises(ValueError):
            test_user = User("Mike", "Moore", 22, '195',5,10)

    def test_invalid_weight_MAX(self):
        with self.assertRaises(ValueError):
            test_user = User("Mike", "Moore", 22, 1001,5,10)

    def test_invalid_weight_MIN(self):
        with self.assertRaises(ValueError):
            test_user = User("Mike", "Moore", 22, -3,5,10)







if __name__ == '__main__':
    unittest.main()
