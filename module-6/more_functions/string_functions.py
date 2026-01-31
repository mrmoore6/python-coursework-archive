"""
Author: Michael Moore
Date: 10/5/20

This program takes a number and a string and returns the string times the number
"""
def multiply_string(n, message):
    """
    :param n: number parameter
    :param message: string parameter
    :return: returns message varible
    """
    for i in range(0, n):
        message = message * n
        return(message)

if __name__ == '__main__':
    print(multiply_string(4, "Mike"))



