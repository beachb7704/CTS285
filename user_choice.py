#// CTS 285
#// M1HW
#// Brenda Beach
#// August 21, 2023

from main import *
from calculator import *


class user_input():
    def start_menu():
          print("1. Add \n"
               "2. Subtract \n"
               "3. Multiply \n"
               "4. Divide \n"
               "5. Exit")
          options = input("Please enter your selection: ")
          #options = int(options)
          
          
          try:
               options = int(options)
               if options == 1:
                    #options = int(options)
                    try:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number:"))
                         #calc.add(num1, num2)
                    except ValueError:
                         print("Please enter a valid number")
                         user_input.start_menu()     
              
               elif options == 2:
                    #options = int(options)
                    try:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number:"))
                    except ValueError:
                         print("Please enter a valid number")
                         user_input.start_menu() 
              
               elif options == 3:
                    #options = int(options)
                    try:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number:"))
                    
                    except ValueError:
                         print("Please enter a valid number")
                         user_input.start_menu() 
               
               elif options == 4:
                    #options = int(options)
                    try:
                         num1 = int(input("Please enter your first number: "))
                         num2 = int(input("Please enter your second number:"))
                    
                    except ValueError:
                         print("Please enter a valid number")
                         user_input.start_menu() 
                              
               elif options == 5:
                    print("Thank you for using my calculator program.")
                    exit()
               
               else:
                    print("Please enter a number between 1 and 5.")
                    user_input.start_menu()
          except ValueError:
               print("Please enter a proper number")
               user_input.start_menu()
               
               
               
               
     




