# from lesson_5 import greetings as g
# import lesson_5
#
# greetings('Aza')
# lesson_5.greetings('Sam')
# g('Beka')


import pprint
import random
from random import randint, choice
from datetime import datetime
import time




def greetings(name):
    hours = datetime.now().hour
    if hours >= 4 and hours <= 11:
        print(f'Good morning! {name}')
    if hours >= 12 and hours <= 17:
        print(f'Good day! {name}')
    if hours >= 18 and hours <= 23:
        print(f'Good evening! {name}')


greetings('Aza')



# print(datetime.now())
# time.sleep(5)
print(datetime.now().hour)



guys = ['Jack', 'Alice', 'Murat', 'Anna', 'Gregoriy']

a = {
    1: 5,
    2: 6

}



start = datetime.now()



# pprint.pprint(random.sample(guys, 2))
# print(randint(1, 5))
# print(choice(guys))
# print(random.a)










