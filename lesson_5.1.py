abiturients1 = [
    {'name': 'Mike', 'ORT': 150},
    {'name': 'Seed', 'ORT': 220},
    {'name': 'Frank', 'ORT': 90}
]

abiturients2 = [
    {'name': 'Arthur', 'ORT': 150},
    {'name': 'Bob', 'ORT': 220},
    {'name': 'John', 'ORT': 90}
]

def list_students(list):
    for i in list:
        for k, v in i.items():
            print(f'{k}: {v}')

#list_students(abiturients1)
list_students(abiturients2)


def add_students(list, name, ORT):
    list.append(dict(name=name, ORT=ORT))
    list_students(list)

add_students(abiturients2, 'Paul', 160)

def delete_students(list, name):
    for i in list:
        if name.title() == i['name']:
            delete_students = list.pop(list.index(i))
            print(f"{delete_students['Seed']} Was deleted")

 list_students(list)

delete_students(abiturients1)

while True:
    user = input()

    if user == 1:
        add_students()





