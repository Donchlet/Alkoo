# arr_1 = [76, 98, 122, 34, 5, 98, 14, 8]
#
# def sort(array):
#     swapped = False
#     for i in range(len(array) -1, 0, -1):
#         for j in range(i):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#         else:
#             break
#     return array
#
#
# print(f'Sorted list: {sort(arr_1)}')



def quick_sort(array):
    if len(array) <= 1:
        return array
    element = array[0]
    left = list(filter(lambda num: num < element, array))
    center = [nums for nums in array if array == element]
    right = list(filter(lambda num: num > element, array))

    return left + center + right


arr_1 = [76, 98, 122, 34, 5, 90, 14, 8]


print(f'Sorted list: {quick_sort(arr_1)}')


list_1 = ('Elle', 'Adi', 'Lol')

for i in list_1:
    if i == 'Elle':
        # print(i)
        pass

list_2 = [i for i in list_1 if i == 'Elle']
print(list_2)
for i in range(20):
    if i % 2 == 0:
        print(i)

list_3 = [num for num in range(20) if num % 2 == 0]

print(list_3)