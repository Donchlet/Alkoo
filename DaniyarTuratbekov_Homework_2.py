"""
Задача №1 "Наследование"
"""
class Weapon:
    def __init__(self, name, damage, ammo, speed):
        self.name = name
        self.damage = damage
        self.ammo = ammo
        self.speed = speed

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Damage: {self.damage}\n' \
               f'Ammo: {self.ammo}\n' \
               f'Speed: {self.speed}\n'

    def danger(self, danger):
        return f'Any weapon can be very {danger}, even for host'
    def license(self, license):
        return f'You need a special {license} to wear any weapon legally\n'
class Pistol(Weapon):
    def __init__(self, name, damage, ammo, speed, light, easy_to_usage):
        super(Pistol, self).__init__(name, damage, ammo, speed)
        if isinstance(light, bool):
            self.light = light
        else:
            raise ValueError('The light weight should be bool!')
        if isinstance(easy_to_usage, bool):
            self.usage = easy_to_usage
        else:
            raise ValueError('The usage should be bool!')
    def advantage(self, comfortable):
        return f'The pistol is pretty {comfortable} to use'
    def lack(self, weak):
        return f'But the pistol is {weak} than assault rifles\n'
    def __str__(self):
        return super(Pistol, self).__str__() + f'Easy in usage: {self.usage}\n\n' \
                                               f'The pistol is {self.name} and ' \
                                               f'its light weight is {self.light}'

class Assault_rifle(Weapon):
    def __init__(self, name, damage, ammo, speed, noise):
        super(Assault_rifle, self).__init__(name, damage, ammo, speed)
        if isinstance(noise, bool):
            self.noise = noise
        else:
            raise ValueError('The noise should be bool!')
    def plus(self, strong):
        return f'The assault rifle is {self.name} and its high level of noise is {self.noise}\n' \
               f'The assault rifle is pretty {strong}'
    def minus(self, heavy):
        return f'But the assault rifle is {heavy} to wear'
    def __str__(self):
        return super(Assault_rifle, self).__str__() + f'Noise: {self.noise}\n'

rifle = Weapon('The Dragunov sniper rifle', 60, 20, 3)
glock = Pistol('Glock', 20, 17, 5, True, True)
ak = Assault_rifle('AK', 80, 40, 30, True)

print(rifle)
print(rifle.danger('dangerous'))
print(rifle.license('license'))
print(glock)
print(glock.advantage('comfortable'))
print(glock.lack('weaker'))
print(ak)
print(ak.plus('strong'))
print(ak.minus('heavy'))

"""
Задача №2 "Инкапсуляция"
"""
class Chat:
    def __init__(self, name, surname, write, change):
        self.name = name
        self.surname = surname
        self._write = write
        self.__change = change

    def _private(self):
        print("Only the members can use the voice button!")
    def __rule(self):
        print('...')

viewer = Chat(name='John', surname='Alderson', write='not yet', change='something')

"""
Задача №3 "Полиморфизм"
"""
class American:
    def give_money(self):
        print('Dollars')

class Russian:
    def give_money(self):
        print('Rubles')

class European:
    def give_money(self):
        print('Euros')

"""
Задача №4 "Полиморфизм с наследованием"
"""

class MartialArts:
    def __init__(self, name, country, method):
        self.name = name
        self.country = country
        self.method = method

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Country: {self.country}\n' \
               f'Method: {self.method}\n'

class Boxing(MartialArts):
    def trick(self):
        return f'Use in fights {self.method}'

class Karate(MartialArts):
    def trick(self):
        return f'Use in fights {self.method}'

class MuayThai(MartialArts):
    def trick(self):
        return f'Use in fights {self.method}'


