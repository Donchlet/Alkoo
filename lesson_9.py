class Phone:
    def __init__(self, number, camera, screen, CPU, memory, touch, flash):
        if isinstance(number, str):
            self.number = number
        else:
            raise ValueError('Number is not ')
        if isinstance(camera, float):
            self.camera = camera
        else:
            raise ValueError('Camera should be float')
        if isinstance(screen, bool):
            self.screen = screen
        else:
            raise Exception('Screen is boolean!!!')
        if isinstance(CPU, float):
            self.cpu = CPU
        else:
            raise ValueError('CPU is float!!!')
        if isinstance(memory, int):
            self.memory = memory
        else:
            raise Exception('Memory is integer')
        if isinstance(touch, bool):
            self.touch = touch
        else:
            raise ValueError('Touch is boolean')
        if isinstance(flash, bool):
            self.flash = flash
        else:
            raise ValueError('Flash is boolean')

    def __str__(self):
        return f'Number: {self.number}\n' \
               f'Camera: {self.camera}\n' \
               f'Screen: {self.screen}\n' \
               f'CPU: {self.cpu}\n' \
               f'Memory: {self.memory}\n' \
               f'Touch: {self.touch}\n' \
               f'Flash: {self.flash}\n'








nokia_6300 = Phone('+996666321', 1.2, False, 0.7, 517, False, True)
print(nokia_6300)

class iPhone(Phone):
    def __init__(self):









