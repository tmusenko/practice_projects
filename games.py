import random

money = 100

# Write your game of chance functions here

# Coin flip game


def coin_flip(guess, bet):
    if(bet <= 0):
        print("Your bet should be more than 0..")
        print("..................................")
        return 0

    print("Lets play flip the coin...!")
    print("You bet on: " + str(guess))
    result = random.randint(1, 2)

    if(result == 1):
        print("The result is Heads")
    elif(result == 2):
        print("The result is Tails")

    if(guess == "Heads" and result == 1) or (guess == "Tails" and result == 2):
        print("You won " + str(bet) + " pounds!")
        print("..................................")
        return bet

    else:
        print("You lost " + str(bet)+" dollars!")
        print("..................................")
        return -bet

# Cho-Han


def cho_han(guess, bet):
    if (bet <= 0):
        print("The bet should be more than 0")
        return 0

    print("Lets play Cho-Han...!")
    print("You bet on: " + str(guess))
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    result = d1 + d2
    print("The sum of two dices is " + str(result))

    if (guess == "Even" and result % 2 == 0):
        print("You won " + str(bet) + " pounds!")
        print("..................................")
        return bet

    elif (guess == "Odd" and result % 2 == 1):
        print("You won " + str(bet) + " pounds!")
        print("..................................")
        return bet

    else:
        print("You lost " + str(bet) + " pounds!")
        print("..................................")
        return -bet


# Higher card

def higher_card(bet):
    if(bet <= 0):
        print("Bet should be more than 0")
        return 0

    print("Lets play card game...!")
    cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5,
             5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]
    mine = random.randint(0, len(cards))
    cards.remove(cards[mine])
    his = random.randint(0, len(cards))
    print("Mine card is " + str(cards[mine]))
    print("His card is " + str(cards[his]))

    if (mine > his):
        print("You won " + str(bet) + " pounds!")
        print("..................................")
        return bet

    elif (mine < his):
        print("You lost " + str(bet) + " pounds!")
        print("..................................")
        return -bet

    else:
        print("It was a tie")
        print("..................................")
        return 0

# Roullete


def roullete(guess, bet):
    if (bet <= 0):
        print("You need to bet more than 0")
        return 0

    print("Lets play roulette...!")
    print("You bet on: " + str(guess))
    result = random.randint(0, 37)
    if(result == 37):
        print("Ball lands on 00")
    else:
        print("Ball lands on: " + str(result))

    if(guess == "Even" and result % 2 == 0 and result != 0):
        print("You won! " + str(bet) + " pounds!")
        print("..................................")
        return bet

    elif(guess == "Odd" and result % 2 == 1 and result != 37):
        print("You won! " + str(bet) + " pounds!")
        print("..................................")
        return bet

    elif(guess == result):
        print("you won! " + str(bet*35) + " pounds!")
        print("..................................")
        return bet * 35

    else:
        print("You lost " + str(bet) + " pounds!")
        print("..................................")
        return -bet


# Call your game of chance functions here
if(money > 0):
    money += coin_flip("Tails", 100)
else:
    print("You dont have enough money to bet...sorry you lost everything..")
    print("Your total amount of money is " + str(money))
    exit()


if(money > 0):
    money += cho_han("Odd", 100)
else:
    print("You dont have enough money to bet...sorry you lost everything..")
    print("Your total amount of money is " + str(money))
    exit()


if(money > 0):
    money += higher_card(20)
else:
    print("You dont have enough money to bet...sorry you lost everything..")
    print("Your total amount of money is " + str(money))
    exit()


if(money > 0):
    money += roullete(12, 12)
else:
    print("You dont have enough money to bet...sorry you lost everything..")
    print("Your total amount of money is " + str(money))
    exit()

print("Your total amount of money is " + str(money))
