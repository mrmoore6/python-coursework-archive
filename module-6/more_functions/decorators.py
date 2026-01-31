def hello_world(name):
    world = "Hello to the world {}".format(name)
    print(world)

def beautiful():
    def add_Mike():
        print(hello_world("!"))
        return "Mike"
    print(hello_world(add_Mike()))

if __name__ == '__main__':
    print(beautiful())

