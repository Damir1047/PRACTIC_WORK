# замыкания

def main_fun(value):
    name = value
    def inner_fun():
        print('hello my friend', name)

    return inner_fun