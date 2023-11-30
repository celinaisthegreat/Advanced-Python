import random
def guess():
    num = random.randint(1,100)
    attempts = 0
    while True:
        user = int(input("choose a number from 1-100:  "))
        if user > num:
            print("try a lower number")
            attempts +=1
        elif user < num:
            print("try a higher number")
            attempts +=1
        else:
            attempts +=1
            print(f"you got the number! the number was {num}. you got it in {attempts} tries")
            break

guess()
