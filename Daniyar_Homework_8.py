import random
import datetime

name = input('Please enter your name: ')
attempt = int(input('Please enter a number of your attempts: '))
attempt_d = attempt
start = datetime.datetime.now()
with open('results.txt', 'w', encoding='UTF-8') as file:
    while attempt != 0:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        v = a*b
        try:
            answer = int(input(f'{a} * {b} = ?'))
            attempt -= 1
            if answer == v:
                print(f'Right answer: {v}')
                print(f'Remaining: {attempt} attempts')
                file.write(f'{a} * {b} ={answer} ({v})- right\n')
            else:
                print(f'Right answer: {v}')
                print(f'Remaining: {attempt} attempts')
                file.write(f'{a} * {b} ={answer} ({v})- not right\n')
        except ValueError:
            print('Only integers!')
    time = datetime.datetime.now() - start
    file.write(f'Was {attempt_d} attempts, spent time: {time}, name: {name}\n')