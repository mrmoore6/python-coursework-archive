"""
NAME: Michael Moore
Date: 1/27/21
This program takes in input and return a calulated insurance quote.
"""
def drivers_name():
    drivers_name = input("Enter Name")
    if not drivers_name.isalpha():
        raise ValueError
    return drivers_name

def accidents(coverage_rate):
        coverage_rate = .41 * coverage_rate + coverage_rate
        return coverage_rate
def discounts(coverage_rate):
    coverage_rate = .10 * coverage_rate
    return coverage_rate

def coverage_level():
    try:
        age = int(input("ENTER AGE"))
    except:
        raise ValueError
    coverage_level = input("Enter Coverage Level, SM, L, F")
    acc = input("ANY Accidents? Y/N")
    discount = input("Do you want a 10% discount? Y/N")
    coverage_rate = 0
    if int(age >= 16 and age < 25) and coverage_level == "SM":
        coverage_rate = 2593
        if acc == "Y" and discount == "N":
            coverage_rate = 2593
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 2593
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 2593
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 2593
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age,coverage_rate,coverage_level)
    elif(age >= 16 and age < 25) and coverage_level == "L":
        coverage_rate = 2957
        if acc == "Y" and discount == "N":
            coverage_rate = 2957
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 2957
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 2957
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 2957
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age,coverage_rate,coverage_level)
    elif (age >= 16 and age < 25) and coverage_level == "F":
        coverage_rate = 6930
        if acc == "Y" and discount == "N":
            coverage_rate = 6930
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 6930
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 6930
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 6930
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 25 and age < 35) and coverage_level == "SM":
        coverage_rate = 608
        if acc == "Y" and discount == "N":
            coverage_rate = 608
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 608
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 608
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 608
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 25 and age < 35) and coverage_level == "L":
        coverage_rate = 691
        if acc == "Y" and discount == "N":
            coverage_rate = 691
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 691
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 691
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 691
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 25 and age < 35) and coverage_level == "F":
        coverage_rate = 1745
        if acc == "Y" and discount == "N":
            coverage_rate = 1745
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 1745
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 1745
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 1745
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 35 and age < 45) and coverage_level == "SM":
        coverage_rate = 552
        if acc == "Y" and discount == "N":
            coverage_rate = 552
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 552
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 552
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 552
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 35 and age < 45) and coverage_level == "L":
        coverage_rate = 627
        if acc == "Y" and discount == "N":
            coverage_rate = 627
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 627
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 627
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 627
        return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 35 and age < 45) and coverage_level == "F":
        coverage_rate = 1564
        if acc == "Y" and discount == "N":
            coverage_rate = 1564
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 1564
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 1564
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 1564
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 45 and age < 55) and coverage_level == "SM":
        coverage_rate = 525
        if acc == "Y" and discount == "N":
            coverage_rate = 525
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 525
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 525
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 525
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 45 and age < 55) and coverage_level == "L":
        coverage_rate = 596
        if acc == "Y" and discount == "N":
            coverage_rate = 596
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 596
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 596
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 596
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 45 and age < 55) and coverage_level == "F":
        coverage_rate = 1469
        if acc == "Y" and discount == "N":
            coverage_rate = 1469
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 1469
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 1469
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 1469
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 55 and age < 65) and coverage_level == "SM":
        coverage_rate = 494
        if acc == "Y" and discount == "N":
            coverage_rate = 494
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 494
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 494
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 494
        return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 55 and age < 65) and coverage_level == "L":
        coverage_rate = 560
        if acc == "Y" and discount == "N":
            coverage_rate = 560
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 560
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 560
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 560
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 55 and age < 65) and coverage_level == "F":
        coverage_rate = 1363
        if acc == "Y" and discount == "N":
            coverage_rate = 1363
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 1363
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 1363
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 1363
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 65) and coverage_level == "SM":
        coverage_rate = 515
        if acc == "Y" and discount == "N":
            coverage_rate = 515
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 515
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 515
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 515
        return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 65) and coverage_level == "L":
        coverage_rate = 585
        if acc == "Y" and discount == "N":
            coverage_rate = 585
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 585
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 585
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 585
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    elif (age >= 65) and coverage_level == "F":
        coverage_rate = 1402
        if acc == "Y" and discount == "N":
            coverage_rate = 1402
            coverage_rate = accidents(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "N":
            coverage_rate = 1402
            coverage_rate = coverage_rate - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        elif discount == "Y" and acc == "Y":
            coverage_rate = 1402
            coverage_rate = accidents(coverage_rate) - discounts(coverage_rate)
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
        else:
            coverage_rate = 1402
            return "AGE: {}, COVERAGE RATE: {}, COVERAGE LEVEL: {}".format(age, coverage_rate, coverage_level)
    else:
        return "ENTER VALID INFO"





def quote():
    my_dict = {"NAME":drivers_name(),
               "COVERAGE INFO":coverage_level()
               }
    print(my_dict)


quote()
