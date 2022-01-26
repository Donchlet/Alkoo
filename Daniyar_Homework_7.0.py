import random
import datetime
import sys
попытка = 0
start = datetime.datetime.now()
numbers = random.randint(1, 101)
#result = random.randrange(numbers)
def listofnumbers(list=numbers):
    while True:
        random.randrange(numbers)
        print(random.randrange(numbers))
        i = input("Попытайтесь отгадать число: ")
        if result == random.randrange(numbers):
            print('Ура! Вы выиграли игру! $$$')
            end = datetime.datetime.now() - start
            print('Конец игры\n'
                  ''f'Время: {end}')
            break
        if i == 'выйти':
            print('Конец игры')
            sys.exit()
        try:
            i == int(i)
        except IndexError:
            print(f'Пожалуйста, не вводите числа, которые меньше 0 и больше')
        except ValueError:
            print('Пожалуйста, не вводите буквы')
        if result != random.randrange(numbers):
            print("Упс, вы ошиблись... Попытайтесь снова")
        elif result > random.randrange(numbers):
            print("Очень близко")
        elif result < random.randrange(numbers):
            print("Очень далеко")
listofnumbers()





















