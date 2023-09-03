import random

def value():
    while True:
        user = int(input("0 for Rock, 1 for Paper, 2 for Scissor\nEnter :"))
        if user == 0 or user == 1 or user == 2:
            return user
        else:
            print("Select appropriate choice")

def check(user,comp):
    if user == comp:
        return -1
    elif comp == 0 and user == 1:
        return 1
    elif comp == 1 and user == 2:
        return 1
    elif comp == 2 and user == 0:
        return 1
    else:
        return 0

def game():
    while True:
        user = value()
        comp = random.randint(0, 2)
        score = check(user,comp)
        if score == -1:
            print("Its a Draw")
        elif score == 1:
            print("You Won")
        else:
            print("You Lose")

        print("You : ", user)
        print("Computer : ", comp)

        another_round = input("Do you want to play another round? (yes/no): ").lower()
        if another_round != "yes":
            break
    print("Thankyou for playing!")
game()
