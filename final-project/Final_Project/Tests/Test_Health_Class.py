import unittest
from Final_Project.Classes import Health_Class as h

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_user = h.Health("Mike","Moore",20,190.5,5,10,2000,100)

    def tearDown(self):
        del self.test_user

    def test_valid_Calorie_Intake(self):
        self.assertEqual(self.test_user.Calories_In, 2000)

    def test_valid_Calorie_Out(self):
        self.assertEqual(self.test_user.Calories_Out, 100)

    def test_valid_BMI(self):
        self.assertEqual(self.test_user.bmi(), 27.3)

    def test_invalid_Calorie_Intake(self):
        with self.assertRaises(ValueError):
            testuser = h.Health("Mike", "Moore", 20, 190.5, 5, 10, -2000, 100)

    def test_invalid_Calorie_Out(self):
        with self.assertRaises(ValueError):
            testuser = h.Health("Mike", "Moore", 20, 190.5, 5, 10, 2000, -2)

    def test_invalid_Calorie_Intake_alpha(self):
        with self.assertRaises(ValueError):
            testuser = h.Health("Mike", "Moore", 20, 190.5, 5, 10, '20f0', 100)

    def test_invalid_Calorie_Out_alpha(self):
        with self.assertRaises(ValueError):
            testuser = h.Health("Mike", "Moore", 20, 190.5, 5, 10, 2000, 'dw32')

    def test_invalid_height_BMI(self):
        with self.assertRaises(ValueError):
            testuser = h.Health("Mike", "Moore", 20, 190.5, 100, 10, 2000, 100)

    def test_invalid_weight_BMI(self):
        with self.assertRaises(ValueError):
            testuser = h.Health("Mike", "Moore", 20, 4590.5, 100, 10, 2000, 100)


if __name__ == '__main__':
    unittest.main()
