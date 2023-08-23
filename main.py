#// CTS 285
#// M1HW
#// Brenda Beach
#// August 21, 2023

#Importing all the functions in the calculator method
from calculator import *
from user_choice import *


def menu():
        options = input("1. Add \n"
             "2. Subtract \n"
             "3. Multiply \n"
             "4. Divide \n"
             "5. Exit \n"
             "Please enter your choice: ")
        print(options)
menu()





num1 = 20
num2 = 2


calculator.add(num1, num2)
calculator.subtract(num1, num2)
calculator.multiply(num1, num2)
calculator.divide(num1, num2)