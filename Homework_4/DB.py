import sqlite3

conf_data = sqlite3.connect("data.sqlite3")
personal_data = conf_data.cursor()

personal_data.execute(
    """CREATE TABLE IF NOT EXISTS users (
    data TEXT, 
    answers TEXT
    )
    """
)
conf_data.commit()


def info():
    global data_of_user
    data_of_user = input('Please enter your data and time: ')

    personal_data.execute(f"SELECT data FROM users WHERE data = '{data_of_user}'")
    if personal_data.fetchone() is None:
        personal_data.execute("INSERT INTO users VALUES (?, ?)", (data_of_user, "no"))
        conf_data.commit()
        print('The box of data is marked')
    for value in personal_data.execute("SELECT * FROM users"):
        print(value)
    else:
        print('Oops, the note already exists!')
        conf_data.commit()

# if __name__ == '__main__':
#     data_user()

def eraser():
    for value in personal_data.execute("SELECT * FROM users"):
        print(value)
    answer = input('Please select a note: ')
    personal_data.execute(f"SELECT data FROM users WHERE data = '{answer}'")
    if personal_data.fetchone():
        choice = input("Done or not?(yes or no)")
        if choice == 'yes':
            personal_data.execute(f"DELETE FROM users WHERE data = '{answer}'")
            print('The note has deleted')
        elif choice == 'no':
            print('The note has saved')
            conf_data.commit()


if __name__ == '__main__':
    eraser()