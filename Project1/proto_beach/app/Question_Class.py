from tabulate import tabulate

class Question():

    def __init__(self, quest_num, num1, operator, num2, ans, T_F):

        self.quest_num = int(quest_num)
        self.num1 = int(num1)
        self.operator = operator
        self.num2 = int(num2)
        self.ans = int(ans)
        self.quest_true = bool(T_F)

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

        return tabulate([["Question Number:", str(self.quest_num)],
                          ["1st Number:", str(self.num1)],
                          ["Operator:", self.operator],
                          ["2nd Number:", str(self.num2)],
                          ["Answer:", str(self.ans)]])




