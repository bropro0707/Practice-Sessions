# GUESS THE NUMBER GAME
import random
print("You have to guess a number between 1,10 for win")
print("you have 5 chances")
ans = "y"
while ans == "y":
    chance = 0
    while(chance < 5):
        guess = int(input("enter the number: "))
        if guess < 1 or guess > 11:
            print("guess is out of range")
            break
        computer = random.randint(1,11)
        if(guess == computer):
            print("you guess correct, you win")
            break
        else:
            print ("wrong guess try again")
            chance += 1
    if chance == 5:
        print("Sorry, you've used all your chances. Better luck next time!")
        ans = input("want to play again: (y/n)")
