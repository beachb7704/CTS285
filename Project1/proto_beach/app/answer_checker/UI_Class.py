from Question_Class import Question
from Answer_Checker import Answer_Checker

# UI class
class UI():

    def __init__(self):
        pass

    def mainMenu():
     
         """ 
         This function displays the main menu to the user. 
         
         inputs: none
         outputs: sent (user selection/sentinel value) and displays main menu
         """
         
         while True:
             
             # Ask the user to choose one of the options.
             try:
                 choice = int(input("\n-- The Adventures of Luna and Mathmaticus --\n"\
                                    "1) Answer Checker\n"\
                                    "2) Memory Bank\n"\
                                    "3) Flash Cards\n"\
                                    "0) Exit\n"\
                                    "--------------------------------------------\n"\
                                    "Enter your choice:\t"))
                     
             # If the user does not enter an int, display an error message.
             except ValueError:
                 print("\nPlease input a valid integer value.")
             
             # General error statement.
             except:
                 print("General Error.")
             
             # Int input validation. 
             else:
                 
                 # If the user's input is an integer but not and appropriate choice: 
                 if (choice > 2 or choice < 0):
                     UI.errorMessage()
                     UI.mainMenu()
                 
                 # If the user's input passes the previous validation steps, break the while loop and 
                 # return "sent" (the sentinel value).
                 else:
                     break
         
         return choice
     
    def eqn_prompt(quest_num):
    
        num1 = int(input(f"{'Enter first number:':<24}"))
        operator = input(f"{'Enter math operator:':<24}")
        num2 = int(input(f"{'Enter second number:':<24}"))
        ans = int(input(f"{'Enter the answer:':<24}"))
    
        if Answer_Checker.right_or_wrong_var(num1,operator,num2, ans):
            # Create the Question object
            return Question(quest_num, num1, operator, num2, ans, True)
        
        # print("The equation you entered is incorrect. Please try again.")
        return Question(quest_num, num1, operator, num2, ans, False)
    
    # def string_parse(i, quest_dict):
    #     quest = input("Enter Question " + str(i) + ":\n")
        
    #     quest = quest.split("=")

    #     # # Check to see if the question is correct
    #     if eval(quest[0]) == int(quest[1]):
            
    #         quest_dict.update({str(i):quest})
    #         i += 1
            
    #=====================#
    def errorMessage():
    #=====================#
    
        """ 
        This function lets the user know that the option chosen is not in the menu. 
        
        inputs: none
        outputs: displays error message and the main menu
        """
        
        print("\nError:  Your choice is not valid.  Please enter a corrrect value.")
    
    #=====================#    
    def generalError():
    #=====================#
    
        """
        This function lets the user/developer know that a general error has occurred A general error
        is one not explicitly stated by the exception handling.
        
        inputs:  none
        outputs: general error message
        """
    
        print("General Error.")
        
    #===============#
    def repeat():
    #===============#
    
        """
        This function asks the user if he wants to repeat the same type of calculation or if he 
        wants to return to the main menu.
        
        inputs:  none
        outputs:  cont (continuation variable)
        """
        while True:
            try:
                # Asking the user how he wants to proceed.
                cont = int(input(("1. Repeat\n" \
                                  "2. Main Menu\n" \
                                  "Enter a number: ")))
                
                # If the user does not enter 1 or 2.
                if (cont < 1 or cont > 2):
                    raise ValueError
            
            # If the user does not enter an appropriate int, display an
            # error message.
            except ValueError:
                
                UI().errorMessage()
            
            # Catch-all general error.
            except:
                UI().generalError()
                
            else:
                break
        
        return cont