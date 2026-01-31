"""
Author: Michael Moore
Program: basicIO.py
Date: 10/11/20

"""
FILE_NAME = 'student_info.txt'
MIN = 0
MAX = 100
EXIT = -1
IO_MSG = "CANNOT OPEN FILE"

def write_to_file(*args):
    print(args)
    try:
        with open(FILE_NAME, 'a') as o:
            o.write('{}, {}: \t'.format(args[1], args[0]))
            for i in args[2]:
                o.write("{}\t".format(i))
            o.write('\n')
    except IOError:
        print(IO_MSG)

def get_student_info(**kwargs):
    print('Hello, {} {}!'.format(kwargs["first_name"], kwargs["last_name"]))
    scores = []
    num = 0
    while num != EXIT:
        try:
            num = float(input("Enter a score between {} and {}, (-1 to exit)".format(MIN, MAX)))
            if num == EXIT:
                break
            elif num < MIN or num > MAX:
                raise ValueError("Score must be between 0 and 100")
            else:
                 scores.append(num)
        except ValueError as error:
            print(error)
    write_to_file(kwargs['first_name'], kwargs['last_name'], scores)

def read_from_file():
    try:
        with open(FILE_NAME, 'r') as o:
            read_line= o.read()
            print(read_line)
    except IOError:
        print(IO_MSG)

if __name__ == '__main__':
    get_student_info(first_name = "Mike", last_name = "Moore")
    get_student_info(first_name = "John", last_name = "Doe")
    input("HOLD UP........")
    read_from_file()
    input("Press any key to end")
