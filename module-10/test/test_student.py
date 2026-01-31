import unittest
from class_definitions import student_class

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = student_class.Student("Moore", "Michael" , 'Math')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, "Michael")
        self.assertEqual(self.student.last_name, "Moore")
        self.assertEqual(self.student.major, "Math")
        self.assertEqual(self.student.gpa, 0.0)

    def test_object_created_all_attributes(self):
        self.student = student_class.Student("Moore", "John", 'Math', 3.4)
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Moore")
        self.assertEqual(self.student.major, "Math")
        self.assertEqual(self.student.gpa, 3.4)


    def test_student_str(self):
        self.assertEqual(str(self.student), "Moore, Michael has major in Math with gpa: 0.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
             test_student = student_class.Student("322d2ddwdw", "Mike","Math", 0.0)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
             test_student = student_class.Student("Mike","322d2ddwdw","Math", 0.0)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
             test_student = student_class.Student("Mike", "Moore","His", 0.0)
    def test_object_not_created_error_gpa_high(self):
        with self.assertRaises(ValueError):
             test_student = student_class.Student("Mike", "Moore","History", 5.0)
    def test_object_not_created_error_gpa_low(self):
        with self.assertRaises(ValueError):
            test_student = student_class.Student("Mike", "Moore", "History", -1.0)
    def test_object_not_created_non_numeric_error_gpa(self):
        with self.assertRaises(ValueError):
            test_student = student_class.Student("Mike", "Moore","History", "string")



if __name__ == '__main__':
    unittest.main()
