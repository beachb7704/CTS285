# The Answer Checker
from Question_Class import Question
# from UI_Class import UI

class Answer_Checker():
    
    def __init__(self):
        pass
    
    def main(cont, debug):
        
        # While the user wants to continue with the calculation:
        while cont != 2:
            
            # Print option label.
            print("\n |===========================|"\
                  "\n | OPTION 1:  Answer Checker |"\
                  "\n |===========================|\n")
                
            quest_num = 1
            false_eq = False
            tries = 3

            while false_eq == False:
                    
                    # # Prompt the user for the input values
                    # if debug:
                    #     num1 = 1
                    #     operator = "+"
                    #     num2 = 1
                    #     ans = 2
            
                    #     if Answer_Checker.right_or_wrong_var(num1,operator,num2, ans):
                    #         # Create the Question object
                    #         quest = Question(quest_num, num1, operator, num2,ans, True)
                            
                    #     else:
                    #         quest = False
                    #         false_eq = True
                    
                    # else:
                    #     quest = UI.eqn_prompt(quest_num)
                        
                    quest = UI.eqn_prompt(quest_num)
                        
                    if quest.quest_true == True:
                        print(str(quest.num1) + quest.operator + str(quest.num2) + " = " + 
                              str(quest.ans))
                        false_eq = True
                        
                    if tries == 1:
                        
                        print("You have run out of attemps to solve the equation\n")
                        print("The answer is " + str(quest.num1) + quest.operator + str(quest.num2) \
                              + " = " + str(eval(str(quest.num1) + quest.operator + str(quest.num2))) + \
                              "\n")
                        break
                    
                    tries -= 1
                    
            cont = UI.repeat()
    
    def right_or_wrong_obj(quest):    
        # Check to see if the question is correct
        if eval(str(quest.num1) + quest.operator + str(quest.num2)) == quest.ans:
            print("\nThe equation is correct!\n")
            # self.correct = True
            return True
            
        else:
            print("\nThe equation you entered was incorrect.  Please try again.\n")
            # self.correct = False
            return False
        
    def right_or_wrong_var(num1,operator,num2,ans):    
        # Check to see if the question is correct
        if eval(str(num1) + operator + str(num2)) == ans:
            print("\nThe equation is correct!\n")
            # self.correct = True
            return True
            
        else:
            print("\nThe equation you entered was incorrect.  Please try again.\n")
            # self.correct = False
            return False