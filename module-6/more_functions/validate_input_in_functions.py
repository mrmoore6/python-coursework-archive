"""
Author: Michael Moore
Date: 10/5/20
Program: validate_input_in_functions
This program takes 2 different inputs test name and test score and return values in formatted string form.
"""
def score_input(test_name, test_score = 0 , invalid_message = 'Invalid test score, try again!'):
    """
    :param test_name: Name of Test
    :type test_name: String
    :param test_score: Entered int for test the score of the test
    :type test_score: int
    :param invalid_message:
    :return: Returns entered values to strings
    :rtype: String

    """
    #print('{}: {}%'.format(test_name,test_score)
    try:
        if test_score >= 0 and test_score <= 100:
            return'{}: {}%'.format(test_name,test_score)
        else:
             return invalid_message
    except TypeError:
        raise TypeError



if __name__ == '__main__':
    score_input("Math", 4)
