ROCK PAPER SCISSOR GAME IN PYTHON
DATE: 17/08/2021

INTRODUCTION:
Wanna play a rock paper scissor with someone but alone?? Python is there for you. 

CODE:
import random
name=input("enter your name:")
tym=int(input("how many tyms"))
pr=0
pc=0
for i in range(0,tym):
    c=random.choice(["rock","paper","scissor"])
    p=input("ROCK PAPER SCISSOR.....: ")
    if c==p:
        print("NO POINTS BOTH USED THE SAME CHOICE")
    elif c=="rock" and p=="paper":
            print(name,"GOT 1 POINT")
            print("PAPER SMASHED THE ROCK")
            pr+=1
    elif c=="scissor" and p=="rock":
        print(name,"GOT 1 POINT")
        print("ROCK SMACHED THE SCISSOR")
        pr+=1
    elif c=="paper" and p=="scissor":
        print(name,"GOT 1 POINT")
        print("SCISSOR DESTROYED THE PAPER")
        pr+=1
    elif p not in ["rock","paper","scissor"]:
        print("INVALID CHOICE")
    else:
        pc+=1
        print("PYTHON GOT 1 POINT")
        print(c,"DISTROYED THE",p)

print("RESULTS TYM.....")
print(name,"GOT",pr)
print("PYTHON GOT",pc)

if pc>pr:
    print("PYTHON WON")
elif pc<pr:
    print(name.upper(),"WON")
else:
    print("DRAW")
