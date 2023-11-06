from tabulate import tabulate

class Question():
    def __init__(self, num1, operator, num2, ans, T_F):

        self.num1 = int(num1)
        self.operator = operator
        self.num2 = int(num2)
        self.ans = int(ans)
        self.quest_true = bool(T_F)
        
    def __init__(self, row):
        """ init a question from a sqlite row object"""
        #session['eqn'] = json.dumps({"num1": eqn[3], "math_op": eqn[4], "num2": eqn[5], "ans": eqn[6]})
        #self.id = row["id"]
        #self.name = row["name"]
        #self.age = row["age"]
        # row numbers (these are majic numbers so we use constants)
        NUM1 = 3
        MATH_OP = 4
        NUM2 = 5
        ANS = 6
        self.num1 = row[NUM1]
        self.operator = row[MATH_OP]
        self.num2 = row[NUM2]
        self.ans = row[ANS]
        #self.quest_true = #something

    # Getters    
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

        return tabulate([["1st Number:", str(self.num1)],
                          ["Operator:", self.operator],
                          ["2nd Number:", str(self.num2)],
                          ["Answer:", str(self.ans)]])




