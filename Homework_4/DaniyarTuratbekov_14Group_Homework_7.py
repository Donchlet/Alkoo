class Numik:
    while True:
        try:
            st = int(input('Please enter your number: '))
            if st > 999 or st < 100:
                raise ValueError
            break
        except ValueError:
            print('Please only three-digit numbers!')
    if st < 0 or str(st) != str(st)[::-1]:
        print('Oops, it is not a palindrome number')
    else:
        print('Hooray! It is a palindrome number!')