import random
ran_num = random.randint(1,100)
guess = int(input("Enter your number guess:"))
amount_guess = 5
for i in range(amount_guess):
    amount_guess -= 1
    if guess > ran_num:
        print("Nope go lower - you have",amount_guess,"more chances")
        if amount_guess == 0:
            print("sorry, you are out of guess")
            break
        else:
            guess = int(input("Enter your number guess:"))
    elif guess < ran_num:
        print("Nope go Higher - you have",amount_guess,"more chances")
        if amount_guess == 0:
            print("sorry, you are out of guess")
            break
        else:
            guess = int(input("Enter your number guess:"))
    else:
        print("You have guessed the right number:",ran_num)
        break;
if ran_num == guess:
    print("Gameover")
else:
    print("The number was:",ran_num)
    print("Gameover")
