NUMBER GUESSING GAME IN PYTHON

DATE:17/08/2021

INTRODUCTION:
This is a purely luck based game where the gamer has to set the range of numbers and the computer will  select a random number and the gamer has to identify that random number. The gamer is given a specific number of chances as he wishes. If the guess he gives is correct the game is over and he won the game. If the guess is wrong he is given a clue if the guessed number is greater or smaller. He can try till the specific chances.


MODULE USED:
    Random


CODE:


import random
f=int(input("NUMBERS STARTING FROM: "))
t=int(input("TILL"))
g=int(input("HOW MANY GUESSES YOU WANT TO MAKE: "))
a=random.randint(f,t)
for i in range(g+1):
        u=int(input("ANY NUMBER FROM SPECIFIED INPUT: "))
        if u==a:
            print("CONGRATSS!! GOOD JOB")
            break
        elif u!=a:
            if u>a:
                print("YOUR GUESS IN GREATER!")
            elif u<a:
                print("YOUR GUESS IS SMALLER")
        elif i==g+1:
            print("chance over")
            break
