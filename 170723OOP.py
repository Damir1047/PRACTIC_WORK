# объекты (данные и поведение)
# Классы
# Экземпляры классов


class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty", args)

    def show_breed (instance):
        print((f'my breed is {instance.breed}'))

    def show_name (instance):
        if hasattr(instance, 'name'):
            print((f'my name is {instance.name}'))
        else:
            print('nothing')

    def set_value (koshka, value, age = 0):
        koshka.name = value
        koshka.age = age