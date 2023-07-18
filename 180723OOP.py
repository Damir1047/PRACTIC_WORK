# __init__ метод, егорофф канал урок 6

class Cat:

    def __init__(self, name, breed = 'pers', age = 1, color = 'yellow'):
        print('hello new object is', self, name, breed, age, color)
        self.breed = breed
        self.age = age
        self.color = color
        self.name = name