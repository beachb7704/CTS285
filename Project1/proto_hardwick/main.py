# Answer Checker:
# Only need to work with one quest/prob at a time.

# from tabulate import tabulate
from Question_Class import Question
from UI_Class import UI
from Answer_Checker import Answer_Checker


def main():
    debug = False
    # print("Mathmaticus:\n")
    
    # Initialize the sentinel value to zero.
    choice = -1
    
    cont = -1

    # While the user wants to continue to use the program (the sentinel value is not equal to 0):
    while choice != 0:
    
        # Display the main menu to the user.
        choice = UI.mainMenu()
        
        #===========================#
        # OPTION 1:  Answer Checker #
        #===========================#
        
        # If the user chooses option 1:
        if choice == 1:
            
            # Calls the option1 function and sends the initialized cont variable value of -1.
            Answer_Checker.main(-1, debug)
                    
        #========================#
        # OPTION 2:  Memory Bank #
        #========================#
        
        # If the user chooses option 1:
        if choice == 2:
            
            quest_dict = {}
            quest_num = 1
            
            # Print option label.
            print("\n |========================|"\
                  "\n | OPTION 2:  Memory Bank |"\
                  "\n |========================|\n")
            
            while cont != 2:
                    
                false_eq = False
                # tries = 3
    
                while false_eq == False:
                        
                    print("\nQuestion #: ", quest_num)
                    
                    # Prompt the user for the input values
                    if debug:
                        num1 = 1
                        operator = "+"
                        num2 = 1
                        ans = 2
            
                        if Answer_Checker.right_or_wrong_var(num1,operator,num2, ans):
                            # Create the Question object
                            quest = Question(quest_num, num1, operator, num2,ans, True)
                            
                        else:
                            quest = False
                            false_eq = True
                    
                    else:
                        quest = UI.eqn_prompt(quest_num)
                        # print(quest.quest_true)
                        
                    if quest.quest_true == True:
                        # print(str(quest.num1) + quest.operator + str(quest.num2) + " = " + 
                        #       str(quest.ans))
                        false_eq = quest.quest_true
                        quest_dict.update({quest_num : quest})
                        quest_num += 1
                
                cont = UI.repeat()
                
            for i in range(len(quest_dict)):
                # print(i)
                # print(quest_dict[i+1])
                print(f"\nQuestion #: {quest_dict[i+1].quest_num:<5}" + \
                      f"{quest_dict[i+1].num1} + {quest_dict[i+1].num2} = {quest_dict[i+1].ans}")
                
            
        #==============================#
        # OPTION 0:  Exit the program. #
        #==============================#
        
        # If the user chooses option 5:
        elif choice == 0:
            
            # Display a good-bye message and terminate the program.
            print("\nExiting Program.")
    
   
        
# Call the main function.
if __name__ == "__main__":    
    main()