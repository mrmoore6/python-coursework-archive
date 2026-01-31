def do_it_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

@do_it_twice
def message():
    print("Welcome")

message()

