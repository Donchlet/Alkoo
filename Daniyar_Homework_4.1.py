import sys
while True:

     flags = {
       'pl': {'white', 'red', 'white red'},
       'ua': {'blue', 'yellow', 'blue yellow'},
       'ru': {'white', 'blue', 'red', 'white red', 'white blue red'},
       'de': {'black', 'red', 'yellow', 'black red', 'black red yellow'},
       'se': {'blue', 'yellow', 'blue yellow'}}
     flags2 = ('brown', 'pink', 'green', 'gray', 'dark', 'purple', 'orange')
     user = str(input("Please enter any colors: "))
     for name, ing in flags.items():
        if user in ing:
           print(name)
        else:
            print("The flag is not found")
            break

        # elif user in flags2:
        #    print("The flag is not found")
        #    break
        #
        # elif user == 'quit':
        #    print("The program stopped")
        #    sys.exit()
        #    break



