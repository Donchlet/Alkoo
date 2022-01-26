class Animal:
    Class = ['Mammals', 'Insects', 'Reptile']
    def __init__(self, name, colour, age, weight):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name should be string')
        if isinstance(colour, str):
            self.colour = colour
        else:
            raise ValueError('Colour should be string')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age should be integer')
        if isinstance(weight, float):
            self.weight = weight
        else:
            raise ValueError('Weight should be float')

    def __str__(self):
        return f'Kind: {self.name}\n' \
               f'Colour: {self.colour}\n' \
               f'Age: {self.age}\n' \
               f'Weight: {self.weight}\n'


Mammal = Animal('wolf', 'gray', 8, 45.8)
print(Mammal)

class Insects(Animal):
    def __init__(self, kind, colour, age, weight, speed):
        super().__init__(kind, colour, age, weight)
        if isinstance(speed, str):
            self.speed = speed
        else:
            raise ValueError('Speed should be string')

    def __str__(self):
        return super(Insects, self).__str__() + f'Speed: {self.speed} \n'

insect = Insects('bee', 'yellow', 1, 0.3, 'fast')
print(insect)

class Reptile(Animal):
    def __init__(self, name, colour, age, weight, hiss):
        super().__init__(name, colour, age, weight)
        self.hiss = hiss
    def __str__(self):
        return f'Kind: {self.name}\n' \
               f'Colour: {self.colour}\n' \
               f'Age: {self.age}\n' \
               f'Weight: {self.weight}\n' \
               f'Hiss: {self.hiss}\n'

snake = Reptile('snake', 'green', 2, 3.5, hiss='Yes')
print(snake)