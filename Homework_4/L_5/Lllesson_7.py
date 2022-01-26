arr_1 = [76, 98, 122, 34, 5, 98, 14, 8]

def sort(array):
    swapped = False
    for i in range(len(array) -1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array


print(f'Sorted list: {sort(arr_1)}')