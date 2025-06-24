#calculator program
#menu
import os
def addition():
    print("addition of two number")
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    sum = num1 + num2
    print("sum =", sum)

def substraction():
    print("substraction of two number")
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    difference= num1 - num2
    print("difference =", difference)

def division():
    print("divison of two number")
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    quotient = num1 / num2
    print("quotient=", quotient)

def multiplication():
    print("multiplication")
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    product = num1 * num2
    print("product =", product)
while 1:
    
    print("enter 1 for addition")
    print("enter 2 for substraction")
    print("enter 3 for division")
    print("enter 4 for multiplication") 
    print("enter 0 for exit")
    userchoice = int(input("enter your choice "))
    if(userchoice==1):
        addition()
    elif(userchoice==2):
         substraction()
    elif(userchoice ==3):
        division()
    elif(userchoice ==4):
        multiplication()
    elif(userchoice ==0):
        break
    else:
        print("wrong choice")
        input("press enter to continue...")
        os.system('cls')