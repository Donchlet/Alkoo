import sys
while 1:
    a = str(input("Input a word, please: "))
    b = len(a)
    print("Number of letters: ", b)
    vowels = 'Aa, Ee, Ii, Oo, Uu, Yy'
    consotans = 'Bb, Cc, Dd, Ff, Gg, Hh, Jj, Kk, Ll, Mm, Nn, Pp, Qq, Rr, Ss, Tt, Vv, Ww, Xx, Yy, Zz'
    count_v = 0
    count_c = 0
    for i in a:
        if i in vowels:
            count_v+=1
        elif i in consotans:
            count_c+=1
        elif a == 'quit':
            print("The program stopped")
            sys.exit()
            break

    print(f'Vowel {count_v}')
    print('Consonant ',count_c )
    print('Consonant/Vowel ', round(count_v*100/b,2),'% /' , round(count_c*100/b,2),'%')