#// CTS 285
#// M1HW
#// Brenda Beach
#// August 21, 2023


# Import all of the other modules needed to run inside this module
#=============#
# Imports     #
#=============#
from M1HW_Beach_calculator import *



class user_input(): 
     
     '''
     This function displays the main menu to the user. 
     
    inputs: user input 1 thorugh 5
    outputs: received input from the user and then runs the selection function.
    '''  
     
     # Displays a menu asking the user to make a selection.
     #=============#
     # Start Menu  #
     #=============#
     
     def start_menu():
          print("1. Add \n"
               "2. Subtract \n"
               "3. Multiply \n"
               "4. Divide \n"
               "5. Exit")
          options = input("Please enter your selection: ")
          user_input.selection(options)
     
     
     # This will ask the user if they want to repeat the function they just performed or select a new function.
     #==============================#
     # Request Number1 Function     #
     #==============================#  
     def request_num1():
          num1 = input("Please enter your first number: ")
          return num1  
     
     
     # This will ask the user if they want to repeat the function they just performed or select a new function.
     #==============================#
     # Request Number2 Function     #
     #==============================#  
     def request_num2():
          num2 = input("Please enter your second number: ")
          return num2  
     
     
     # This will ask the user to select if they want to repeat function or work on different one.
     #==============================#
     # Repeat Question Function     #
     #==============================#
     def repeat_question():
          answer = input("Would you lke to repeat or perform another function? \n"
               "1. Repeat \n"
               "2. Perform a differnt function \n"
               "Please enter your selection: ")
          return answer
          
          
     
     
     # This will ask the user if they want to repeat the function they just performed or select a new function.
     #=========================#
     # Repeat Add Function     #
     #=========================#
     
     def add_repeat():
          answer = user_input.repeat_question()
          try:
               answer = int(answer)
               if answer == 1:
                    num1 = user_input.request_num1()
                    num1 = float(num1)
                    num2 = user_input.request_num2()
                    num2 = float(num2)
                    Calculations.addition(num1, num2)
                    user_input.add_repeat()
               elif answer == 2:
                    user_input.start_menu()
               else:
                    print("Please enter a 1 or 2.")
                    user_input.add_repeat()
          except ValueError:
               print("Please enter a number: ")
               user_input.add_repeat()
     
     
     
     
     # This will ask the user if they want to repeat the function they just performed or select a new function.
     #==============================#
     # Repeat Subtract Function     #
     #==============================#
     
     def subtract_repeat():
          answer = user_input.repeat_question()
          try:
               answer = int(answer)
               if answer == 1:
                    num1 = user_input.request_num1()
                    num1 = float(num1)
                    num2 = user_input.request_num2()
                    num2 = float(num2)
                    Calculations.subtract(num1, num2)
                    user_input.subtract_repeat()
               elif answer == 2:
                    user_input.start_menu()
               else:
                    print("Please enter a 1 or 2.")
                    user_input.subtract_repeat()
          except ValueError:
               print("Please enter a number: ")
               user_input.subtract_repeat()
     
     
     # This will ask the user if they want to repeat the function they just performed or select a new function.
     #==============================#
     # Repeat Multiply Function     #
     #==============================#
     
     def multiply_repeat():
          answer = user_input.repeat_question()
          try:
               answer = int(answer)
               if answer == 1:
                    num1 = user_input.request_num1()
                    num1 = float(num1)
                    num2 = user_input.request_num2()
                    num2 = float(num2)
                    Calculations.multiply(num1, num2)
                    user_input.multiply_repeat()
               elif answer == 2:
                    user_input.start_menu()
               else:
                    print("Please enter a 1 or 2.")
                    user_input.multiply_repeat()
          except ValueError:
               print("Please enter a number: ")
               user_input.multiply_repeat()
     
     
     # This will ask the user if they want to repeat the function they just performed or select a new function.
     #============================#
     # Repeat Divide Function     #
     #============================#
     
     def divide_repeat():
          answer = user_input.repeat_question()
          
          try:
               answer = int(answer)
               if answer == 1:
                    num1 = user_input.request_num1()
                    num1 = float(num1)
                    num2 = user_input.request_num2()
                    num2 = float(num2)
                    Calculations.divide(num1, num2)
                    user_input.divide_repeat()
               elif answer == 2:
                    user_input.start_menu()
               else:
                    print("Please enter a 1 or 2.")
                    user_input.divide_repeat()
          except ValueError:
               print("Please enter a number: ")
               user_input.divide_repeat()
                    
          
     
     
     # This will take the selection that the user chose from the start_menu function and will run the appropriate function.
     #=========================#
     # Selection Function      #
     #=========================#
     
     def selection(options):
          try:
               options = int(options)
               if options == 1:
                    try:
                         num1 = user_input.request_num1()
                         num1 = float(num1)
                         num2 = user_input.request_num2()
                         num2 = float(num2)
                         Calculations.addition(num1, num2)
                         user_input.add_repeat()
                    except ValueError:
                         print("Please enter a valid number")
                         user_input.selection(options)     
              
               elif options == 2:
                    try:
                         num1 = user_input.request_num1()
                         num1 = float(num1)
                         num2 = user_input.request_num2()
                         num2 = float(num2)
                         Calculations.subtract(num1, num2)
                         user_input.subtract_repeat()
                    except ValueError:
                         print("Please enter a valid number")
                         user_input.selection(options) 
              
               elif options == 3:
                    try:
                         num1 = user_input.request_num1()
                         num1 = float(num1)
                         num2 = user_input.request_num2()
                         num2 = float(num2)
                         Calculations.multiply(num1, num2)
                         user_input.multiply_repeat()
                    except ValueError:
                         print("Please enter a valid number")
                         user_input.selection(options) 
               
               elif options == 4:
                    try:
                         num1 = user_input.request_num1()
                         num1 = float(num1)
                         num2 = user_input.request_num2()
                         num2 = float(num2)
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
          