# замыкания

def main_fun(value):
    name = value
    def inner_fun():
        print('hello my friend', name)

    return inner_fun


def adder(value):

    def inner(a):
        return value+a
        print(a)
        print(value)

    return inner