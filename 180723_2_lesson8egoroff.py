# Моносостояние для всех экземпляров

class Cat:
    shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.shared_attr