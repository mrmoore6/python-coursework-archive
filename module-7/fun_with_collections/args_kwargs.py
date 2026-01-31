from statistics import mean
"""
Author: Michael Moore
Program: args_kwargs.py
Date: 10/11/20

Takes Keyword & Arbitrary Arguments from main as args and kwargs gets the average of args and returns and also prints out the keyworks arguments.
"""
def average_scores(*args, **kwargs,):
    # Use *args for average calculation
    avg = mean(args)
    for key, value in kwargs.items():
       print("%s == %s" % (key, value))
    # return
    return "Average Score {}".format(avg)

if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, student_name='Michael Moore', course_name='Math', course_gpa=3.67))
    print(average_scores(5, 3, 1, 6, 7, 5, 6, student_name='John Doe', course_name='Science', course_gpa=2.0),)
    print(average_scores(6, 2, 5, 3, 2, student_name='John Doe', course_name='Science', course_gpa=4.0))

