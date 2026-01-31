"""
Author: Michael Moore
Program: input_while.py
Date:9/26/20
This program takes and input between 1 and 100 checks if that input is valid and then stores it in a list and use a loop
to print out the list.
"""

#declare a list variable
numbers = [ ]
user = 0
#prompt and get the user input
user_input = float(input("Enter number between 1 and 100 use -1 to stop"))
#while sentinel value is not stopping value
while user_input != -1:
    #while user input is not good ( in range)
    while user_input not in range(1, 100):
        # prompt user for good input
        user_input = float(input("Enter valid input"))
    #store in list
    numbers.append(user_input)
    #prompt and get the next user input
    user_input = float(input("Enter number between 1 and 100 use -1 to stop"))


#print the list using a for loop
for x in numbers:
    print(x)

# Inputed lots of diffent values for loop pulled them out and printed them
