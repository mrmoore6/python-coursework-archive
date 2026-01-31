from multiprocessing import Process, Manager, Pool
import random
from itertools import chain
from time import process_time

my_range = 1000000


def greater_than_five(number):
    return number > 5


def random_list(x):
    rand_list = []
    for i in range(my_range):
        num_list = random.randint(0, 10)
        rand_list.append(num_list)
    y = filter(greater_than_five, rand_list)
    filtered_numbers = list(y)
    return filtered_numbers


def main():
    p = Pool(processes=20)
    data = p.map(random_list, range(1))
    data = list(chain(*data))
    return data

    # for i in range(1):
    # p = Process(target=random_list, args=(i,))
    # p.start()
    # p.join()


if __name__ == "__main__":
    x = main()
    print(len(x))
    print("{} seconds".format(process_time()))
    y = random_list(None)
    print(len(y))
    print("{} seconds".format(process_time()))
