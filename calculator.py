#// CTS 285
#// M1HW
#// Brenda Beach
#// August 21, 2023


from main import *
from user_choice import *


# Class that will perform the functions of the calculator
#===================#
class calc():
#===================#
    def add(num1, num2):
        try:
            answer1 = num1 + num2
            print("result: ", num1, " + ", num2, " = ", answer1)
        except ValueError:
            print("Please enter a valid number")
    def subtract(num1, num2):
        answer2 = num1 - num2
        print("result: ", num1, " - ", num2, " = ", answer2)
    def multiply(num1, num2):
        answer3 =  num1 * num2
        print("result: ", num1, " * ", num2, " = ", answer3)
    def divide(num1, num2):
        try:
            answer4 = num1 / num2
            print("result: ", num1, " / ", num2, " = ", answer4)
        #This error will throw an error if you try to divide a number by zero
        except ZeroDivisionError:
            print("You can't divide by zero")


