while 1:
    a = str(input("Enter a surname, please: "))
    Jewish = ['Goldstein', 'Silverstein', 'Silverman', 'Zuckerberg', 'Schneider', 'Levin', 'Goldman', 'Demant']
    German = ['Lutz', 'Schmidt', 'Muller', 'Fischer', 'Weber', 'Becker', 'Meier', 'Wagner', 'Werner', 'Klein']
    if a in Jewish:
        print('The surname is Jewish')
    elif a in German:
        print('The surname is German')
    elif a == 'quit':
        break
    else:
        print("Excuse me, but the surname is not found...")
