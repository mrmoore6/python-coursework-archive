from statistics import mean
def user(number = 0):
    bad_input = False
    my_list = []
    user_num = input("Enter Number of Intergers")
    if user_num.isdigit():
        user_num = int(user_num)
    else:
        bad_input = True
        try:
            while bad_input == True:
                user_num = int(input("Renter Number of Intergers"))
                if user_num > 1:
                    bad_input = False
        except:
            print("Enter Correct Input")

        user_num = int(user_num)
    while user_num < 1:
        user_num = input("Renter Number of Intergers")
        user_num = int(user_num)
    try:
        for x in range(user_num):
            number = input("Enter Integer")
            if number.isdigit():
                number = int(number)
                my_list.append(number)
            else:
                raise ValueError
        return my_list
    except ValueError:
        print("Enter Correct Input")






def user_avg(list):
    num = 0
    for x in list:
        num = num + x
    avg = num / len(list)
    return "{} average for {}".format(avg,list)

average = user_avg(user())
print(average)




