import sys
while True:
    flags = {
        'pl': {'red', 'white', 'white red'},
        'ua': {'blue', 'yellow', 'blue yellow'},
        'ru': {'red', 'white', 'blue', 'white red', 'white blue', 'blue red', 'blue white', 'white blue red'},
        'de': {'black', 'red', 'yellow', 'yellow red', 'yellow black', 'black yellow', 'black red', 'black red yellow'},
        'se': {'blue', 'yellow', 'blue yellow', 'yellow blue'}}
    user = str(input("Please enter any colors: "))
    for name, ing in flags.items():
        if user in ing:
            print(name)
        elif user == 'quit':
            print("The program stopped")
            sys.exit()