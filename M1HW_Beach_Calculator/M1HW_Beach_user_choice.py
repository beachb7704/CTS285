#// CTS 285
#// M1HW
#// Brenda Beach
#// August 21, 2023

from M1HW_Beach_calculator import *

class user_input():   
     
     def start_menu():
          print("1. Add \n"
               "2. Subtract \n"
               "3. Multiply \n"
               "4. Divide \n"
               "5. Exit")
          options = input("Please enter your selection: ")
          user_input.selection(options)
     
     
     def add_repeat():
          answer = input("Would you lke to repeat or perform another function? \n"
                            "1. Repeat \n"
                            "2. Perform a differnt function \n"
                            "Please enter your selection: ")
          try:
               answer = int(answer)
               try:
                    if answer == 1:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number: "))
                         Calculations.addition(num1, num2)
                         user_input.add_repeat()
                    elif answer == 2:
                         user_input.start_menu()
               except ValueError:
                    print("Please enter 1 or 2.")
          except ValueError:
               print("Please enter a number: ")
     
     
     
     
     
     def subtract_repeat():
          answer = input("Would you lke to repeat or perform another function? \n"
                            "1. Repeat \n"
                            "2. Perform a differnt function \n"
                            "Please enter your selection: ")
          try:
               answer = int(answer)
               try:
                    if answer == 1:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number: "))
                         Calculations.subtract(num1, num2)
                         user_input.subtract_repeat()
                    elif answer == 2:
                         user_input.start_menu()
               except ValueError:
                    print("Please enter 1 or 2.")
          except ValueError:
               print("Please enter a number: ")
     
     
     def multiply_repeat():
          answer = input("Would you lke to repeat or perform another function? \n"
                            "1. Repeat \n"
                            "2. Perform a differnt function \n"
                            "Please enter your selection: ")
          try:
               answer = int(answer)
               try:
                    if answer == 1:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number: "))
                         Calculations.multiply(num1, num2)
                         user_input.multiply_repeat()
                    elif answer == 2:
                         user_input.start_menu()
               except ValueError:
                    print("Please enter 1 or 2.")
          except ValueError:
               print("Please enter a number: ")
     
     
     
     def divide_repeat():
          answer = input("Would you lke to repeat or perform another function? \n"
                            "1. Repeat \n"
                            "2. Perform a differnt function \n"
                            "Please enter your selection: ")
          try:
               answer = int(answer)
               try:
                    if answer == 1:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number: "))
                         Calculations.divide(num1, num2)
                         user_input.divide_repeat()
                    elif answer == 2:
                         user_input.start_menu()
               except ValueError:
                    print("Please enter 1 or 2.")
          except ValueError:
               print("Please enter a number: ")
                    
          
     
     
     
     def selection(options):
          try:
               options = int(options)
               if options == 1:
                    try:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number: "))
                         Calculations.addition(num1, num2)
                         user_input.add_repeat()
                    except ValueError:
                         print("Please enter a valid number")
                         user_input.selection(options)     
              
               elif options == 2:
                    try:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number: "))
                         Calculations.subtract(num1, num2)
                         user_input.subtract_repeat()
                    except ValueError:
                         print("Please enter a valid number")
                         user_input.selection(options) 
              
               elif options == 3:
                    try:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number: "))
                         Calculations.multiply(num1, num2)
                         user_input.multiply_repeat()
                    except ValueError:
                         print("Please enter a valid number")
                         user_input.selection(options) 
               
               elif options == 4:
                    try:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number:"))
                         Calculations.divide(num1, num2)
                         user_input.divide_repeat()
                    except ValueError:
                         print("Please enter a valid number")
                         user_input.selection(options) 
                              
               elif options == 5:
                    print("Thank you for using my calculator program.")
                    exit()
               
               else:
                    print("Please enter a number between 1 and 5.")
                    user_input.start_menu()
               
          except ValueError:
               print("Please enter a proper number")
               user_input.start_menu()
          