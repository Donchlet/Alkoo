Movies = {
    "Godzilla": {
        "Максим": 8,
        "Данила": 7,
        "Александр": 10
    },
    "Freddy vs. Jason": {
        "Чынгыз": 10,
        "Бектур": 8,
        "Эрбол": 9
    },
    "It": {
        "Михаэль": 9,
        "Фрэнк": 7,
        "Джон": 6

    }

}

def list_movies(list, Джон):
    for i in list:
        for k, v in i.items():
            print(f'{k}: {v}')



list_movies(Movies)


def add_movies(list, film):
    list.append(dict(film=film))
    list_movies(list)

add_movies(Movies, 'Panda')


list_movies(list)





