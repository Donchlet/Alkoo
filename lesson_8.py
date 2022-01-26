# file = open('text.txt', 'w')
# file.write('Hi, world')

import time
from random import randint, sample
import datetime

cash = 500

while cash != 0:
    bet = int(input(
        'Введите ставку'
        f'Доступно: {cash}\n'
    ))
    comp = [randint(1, 6), randint(1, 6)]
    user = [randint(1, 6), randint(1, 6)]
    if sum(comp) > sum(user):


# print(sample(range(1, 6), 2))

# print(randint(1, 6), randint(1, 6))







# with open('new_file.txt', 'r', encoding='UTF-8') as file:
#     for i in file.read():
#         print(i, end='')
#         time.sleep(0.2)




# file.close()

# with open('text.txt', 'w') as file:
#     file.write('Python 3.9')
#
# with open('new_text.txt', 'a') as file:
#     file.write('\n Best programming language')





















