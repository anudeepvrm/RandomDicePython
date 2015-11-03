__author__ = 'avarm1'
import random

def Dice1():
    def rollDice():
        number=random.randint(1,6)
        print("your dice number is %d"%number)

    while(True):
        choice = input("\n\nDo you want to roll \n1.Y for yes\n2.N for no")
        if(choice=="y"):
            rollDice()
            Test.hello()
        else:
            break



