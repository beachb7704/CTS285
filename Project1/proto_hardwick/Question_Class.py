#CTS 285 Project1 DataMan 

# thoughts:
# type in whole equation vs individual numbers using eval()
#   how to parse 3+3=6 vs 3 + 3 = 6


# Ask user for question
class Question():
    
    def __init__(self, quest_num, num1, operator, num2, ans, T_F):
        
        self.quest_num = quest_num
        self.num1 = num1
        self.operator = operator
        self.num2 = num2
        self.ans = ans
        self.quest_true = T_F
        
    # Getters
    def get_quest_num(self):
        return self.quest_num
    
    def get_num1(self):
        return self.num1
    
    def get_operator(self):
        return self.operator
    
    def get_num2(self):
        return self.num2
        
    def get_ans(self):
        return self.ans
    
    def get_true(self):
        return self.quest_true
    
    
    # Setters
    def set_quest_num(self, quest_num):
        self.quest_num = quest_num
        
    def set_num1(self, num1):
        self.num1 = num1
        
    def set_operator(self, operator):
        self.operator = operator
        
    def set_num2(self, num2):
        self.num2 = num2
        
    def set_ans(self, ans):
        self.ans = ans
    
    def set_true(self, T_F):
        self.quest_true = T_F
        
        
    # String Representation:    
    def __repr__(self):
        print("Question Number:\t" + str(self.quest_num))
        print("1st Number:\t" + str(self.num1))
        print("Operator:\t" + str(self.operator))
        print("2nd Number:\t" + str(self.num2))
        print("Answer:\t" + str(self.ans))
        print("Correct:\t" + str(self.T_F))
    

# Answer Checker:
# Only need to work with one quest/prob at a time.

def main():
    
    print("Answer Checker:")
        
    # quest_total = int(input("How many question do you want to record?"))
    
    # quest_dict = {}
    
    question = Question()
    
    i = 1
    
    num1 = int(input("Enter first number:\t"))
    operator = input("Enter math operator:\t")
    num2 = int(input("Enter second number:\t"))
    ans = int(input("Enter the answer:\t"))
        
    # Check to see if the question is correct
    if eval(str(num1) + operator + str(num2)) == ans:
        # quest_dict.update({str(i):[num1,operator, num2, ans]})
        question(i, num1, operator, num2, ans, True)
        i += 1
        
    else:
        print("The equation you entered was incorrect.  Please try again.")
        
        # quest = input("Enter Question " + str(i+1) + ":\n")
        
        
        # # Check to see if the question is correct
        # if eval(quest[:5]) == float(quest.split()[-1]):
            
        #     quest_dict.update({str(i):quest.split()})
        #     i += 1
            
        #     # Question(quest, i, True)
            
        # else:
        #     print("The equation you entered was incorrect.  Please try again.")
        
    
    for i in range(quest_total):
        
        print("Question " + Question.get_num(i) + ": " + Question.get_quest())
        
        
# Call the main function.
if __name__ == "__main__":    
    main()