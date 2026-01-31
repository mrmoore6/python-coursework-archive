"""
Author: Michael Moore
Program: input_while.py
Date:9/26/20
This program takes and input between 1 and 100 checks if that input is valid and then stores it in a list and use a loop
to print out the list.
"""

#declare a list variable
numbers = [ ]
user_input = 0
#prompt and get the user input

#while sentinel value is not stopping value
while user_input != -1:
    g_value = False
    #while user input is not good ( in range)
    while not g_value:
        try:
            user_input = float(input("Enter number between 1 and 100 use -1 to stop"))
            if user_input == -1:
                break
            elif user_input < 1 or user_input >100:
                 raise ValueError("Enter valid input")
            else:
               numbers.append(user_input)
               g_value = True
        except ValueError as err:
            print(err)

        # prompt user for good input



    #store in list

    #prompt and get the next user input



#print the list using a for loop
for x in numbers:
    print(x)

#Inputed lots of diffent values for loop pulled them out and printed them
