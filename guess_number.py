import random

def guess_number():
    high=0
    low=0
    win=0
    number=random.randint(0,20)
    while win==0:
        guess_num=int(input("Please guess a number between 0 and 20: "))
        if guess_num > number:
            message="Too high, try again"
            high +=1
        elif guess_num==number:
            message="Congratulations! You got it"
            win+=1
        else:
            message = "Too low, try again."
            low += 1
        print(message)
    print("Total Try :",(high + low + win))
    
    
guess_number()
