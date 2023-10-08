#CTS 285 Project1 DataMan 

# thoughts:
# type in whole equation vs individual numbers using eval()
#   how to parse 3+3=6 vs 3 + 3 = 6

from tabulate import tabulate


# Ask user for question
class Question():

    def __init__(self, quest_num, num1, operator, num2, ans, T_F):
        
        # Check to see if the question is correct
        if eval(str(num1) + operator + str(num2)) == ans:
            self.quest_num = int(quest_num)
            self.num1 = int(num1)
            self.operator = operator
            self.num2 = int(num2)
            self.ans = int(ans)
            self.quest_true = bool(T_F)
            
        else:
            print("The equation you entered was incorrect.  Please try again.")
            return False
        
        
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

        # return "\nQuestion Number:\t" + str(self.quest_num) + \
        #        "\n1st Number:\t" + str(self.num1) + \
        #        "\nOperator:\t" + self.operator + \
        #        "\n2nd Number:\t" + str(self.num2) + \
        #        "\nAnswer:\t" + str(self.ans) + \
        #        "\nCorrect:\t" + str(self.quest_true)

        return tabulate([["Question Number:", str(self.quest_num)],
                         ["1st Number:", str(self.num1)],
                         ["Operator:", self.operator],
                         ["2nd Number:", str(self.num2)],
                         ["Answer:", str(self.ans)],
                         ["Correct:", str(self.quest_true)]])
# The Answer Checker
class Answer_Checker():

    def __init__(self, question):

        self.quest = question

    def answer_checker(self):    
        # Check to see if the question is correct
        if eval(str(self.quest.num1) + self.quest.operator + str(self.quest.num2)) == self.quest.ans:
            print("The equation is correct!")
            self.correct = True
            return True
            
        else:
            print("The equation you entered was incorrect.  Please try again.")
            self.correct = True
            return False
    
    # String Representation:    
    def __repr__(self):
        print("Your question is ", self.correct)

# Answer Checker:
# Only need to work with one quest/prob at a time.

def main():
    debug = True
    print("Answer Checker:\n")
        
    # quest_total = int(input("How many question do you want to record?"))
    
    quest_dict = {}
    
    quest_num = 1
    
    if debug:
        num1 = 1
        operator = "+"
        num2 = 1
        ans = 2
    
    else:
        num1 = int(input("Enter first number:\t"))
        operator = input("Enter math operator:\t")
        num2 = int(input("Enter second number:\t"))
        ans = int(input("Enter the answer:\t"))

    
        
    # Check to see if the question is correct
    if eval(str(num1) + operator + str(num2)) == ans:
        # quest_dict.update({str(i):[num1,operator, num2, ans]})
        T_F = True
        question = Question(quest_num, num1, operator, num2, ans, T_F)
        print("\nGood job! The equation is correct!\n")
        quest_dict.update({str(quest_num):question})
        # quest_num += 1
        
    else:
        print("\nThe equation you entered was incorrect.  \
              Please try again.\n")
        
        # quest = input("Enter Question " + str(i+1) + ":\n")
        
        
        # # Check to see if the question is correct
        # if eval(quest[:5]) == float(quest.split()[-1]):
            
        #     quest_dict.update({str(i):quest.split()})
        #     i += 1
            
        #     # Question(quest, i, True)
            
        # else:
        #     print("The equation you entered was incorrect.  Please try again.")
    
    print(question)
    
    print("Printing question dictionary")
    print(quest_dict["1"])
        
# Call the main function.
if __name__ == "__main__":    
    main()