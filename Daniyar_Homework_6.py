import sys

def filter_numbers(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False


ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
out_filter = filter(filter_numbers, ten)
evens = list(map(lambda x: x ** 2, out_filter))
print(evens)

def obj_index(list=ten):
    while 1:
            index = input('Please enter your index: ')
            if index == 'quit':
                break
            try:
                index = int(index)
                print(list[index])
            except IndexError:
                print(f'Please enter index between 0 and {len(list)-1}')
            except ValueError:
                print("Please do not enter letters!")

obj_index()
obj_index(evens)