import random
import datetime



numbers = random.randint(1, 100)
попытка = 0
end = datetime.datetime.now()
print("Вы начали игру! Удачи!")
while True:
    попытка += 1
    try:
        i = int(input("Попытайтесь угадать число: "))
        if i > 100 or i < 1:
            print("Число находится между 1 и 100")
            continue
    except:
        print("Пожалуйста, не вводите буквы")
        continue
    if (i > numbers):
        if i - numbers <= 5:
            print("Очень близко! Продолжайте")
        elif i - numbers <= 10:
            print("Близко! Продолжайте")
    if (i < numbers):
        if numbers - i <= 5:
            print("Очень близко! Продолжайте")
        elif numbers - i <= 10:
            print("Близко! Продолжайте")
    if i == numbers:
        попытка += 1
        print("Ура! Вы угадали число и выиграли игру! $$$")
        print(f'Загаданное число: {numbers}')
        print(f'Количество попыток: {попытка}')
        end = datetime.datetime.now() - end
        print(f'Проведённое время в игре: {end.seconds}')
        break















