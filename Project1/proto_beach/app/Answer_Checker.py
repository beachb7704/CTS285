# The Answer Checker
from app.Question_Class import Question

class Answer_Checker():
    
    def __init__(self):
        pass
    
    def right_or_wrong_obj(self, quest):  
          
        # Check to see if the question is correct
        if eval(str(quest.num1) + quest.math_op + str(quest.num2)) == quest.ans:
            # print("\nThe equation is correct!\n")
            # self.correct = True
            return True
            
        else:
            # print("\nThe equation you entered was incorrect.  Please try again.\n")
            # self.correct = False
            return False
        
    def right_or_wrong_var(self,num1,math_op,num2,ans): 

        # Check to see if the question is correct
        if eval(str(num1) + math_op + str(num2)) == int(ans):
            # print("\nThe equation is correct!\n")
            # self.correct = True
            return True
            
        else:
            # print("\nThe equation you entered was incorrect.  Please try again.\n")
            # self.correct = False
            return False
        