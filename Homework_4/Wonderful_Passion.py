from Fortune import Fortune
from Logics import Asino

dosh = 10000
chance = 0
while True:
    slot = int(input("Please choose your number: "))
    bid = int(input("Your wager: "))
    attempt = Asino(dosh, chance)
    attempt.game(slot, bid)
    chance = attempt.chance
    print('-' * 40)
    var = input("Do you want to restart the game?: ")
    if var == "Yes":
        continue
    else:
        if attempt.chance > 0:
            print(f"Alas, you lose: ${attempt.chance}")
        else:
            print(f"Alas, you lose: ${attempt.chance}")
        var_2 = input("Do you want to play 'Lucky Monsters'? ")
        if var_2 == "Yes":
            print('-' * 40)
            print("Choose your decision(I believe, I do not believe): ")
            attempt_2 = Fortune()
            attempt_2.game(attempt.chance)
            dosh += attempt_2.result
            print('-' * 40)
            print(f"Your balance is ${dosh}!")
            break
        else:
            dosh += attempt.chance
            print('-' * 40)
            print(f"Your balance is ${dosh}!")
            break
