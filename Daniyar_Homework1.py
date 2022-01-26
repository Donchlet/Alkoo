class Animal:
    def __init__(self, plant_eating, carnivorous, omnivorous):
        if isinstance(plant_eating, str):
            self.plant_eating = plant_eating
        else:
            raise  ValueError('Plant_eating should be string')
        if isinstance(carnivorous, str):
            self.carnivorous = carnivorous
        else:
            raise ValueError('Carnivorous should be string')
        if isinstance(omnivorous, str):
            self.omnivorous = omnivorous
        else:
            raise ValueError('Omnivorous should be string')

    def __str__(self):
        return f'Plant_eating: {self.plant_eating}\n' \
               f'Carnivorous: {self.omnivorous}\n' \
               f'Omnivorous: {self.omnivorous}\n' \


#creature = Animal(plant_eating='No', carnivorous='Yes', omnivorous='Yes')

#print(creature)

class Mammal(Animal):
    def __init__(self, carnivorous, omnivorous, breastfeeding):
        super().__init__(carnivorous, omnivorous, breastfeeding)
        self.breastfeeding = breastfeeding
    def __str__(self):
        return f'Carnivorous: {self.omnivorous}\n' \
               f'Omnivorous: {self.omnivorous}\n' \
               f'Breastfeeding: {self.breastfeeding}\n'

the_brown_bear = Mammal(carnivorous='Yes', omnivorous='Yes', breastfeeding='Yes')

print(the_brown_bear)

class Reptile(Animal):
    def __init__(self, carnivorous, omnivorous, hiss):
        super().__init__(carnivorous, omnivorous, hiss)
        self.hiss = hiss
    def __str__(self):
        return f'Carnivorous: {self.carnivorous}\n' \
               f'Omnivorous: {self.omnivorous}\n' \
               f'Hiss: {self.hiss}\n'

snake = Reptile(carnivorous='No', omnivorous='Yes', hiss='Yes')

print(snake)























