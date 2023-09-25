#CTS 285 Project1 DataMan 


# Ask user for question
class Question():
    
    def __init__(self, quest, num, T_F):
        self.quest = quest
        self.quest_num = num
        # self.quest_parts = None
        self.quest_true = T_F
        
    def get_quest(self):
        return self.quest
        
    def get_num(self):
        return self.quest_num
    
    def get_true(self):
        return self.quest_true
    
    def set_quest(self, quest):
        self.quest = quest
        
    def set_num(self, num):
        self.quest_num = num
    
    def set_true(self, T_F):
        self.quest_true = T_F
    

def main():
        
    quest_total = int(input("How many question do you want to record?"))
    
    # quest_dict = {}
    
    i = 0
    
    while i < quest_total:
        
        quest = input("Enter Question " + str(i+1) + ":\n")
        
        # Check to see if the question is correct
        if eval(quest[:5]) == float(quest.split()[-1]):
            
            # quest_dict.update({str(i):quest.split()})
            i += 1
            
            Question(quest, i, True)
            
        else:
            print("The equation you entered was incorrect.  Please try again.")
        
    
    for i in range(quest_total):
        
        print("Question " + Question.get_num("1") + ": " + Question.get_quest())
        
        
# Call the main function.
if __name__ == "__main__":    
    main()