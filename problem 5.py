import random
pc_number=random.randint(0,100)
guess=0
while True:
    user_number=int(input("please enter a number: "))
    guess+=1

    if pc_number==user_number:
        print("Yay! you won")
        break

    if pc_number>user_number:
        print("pick a bigger number :> ")

    if pc_number<user_number:
        print("you`re up high! come down a little bit")
print("How many time you`ve guessed: ",guess)