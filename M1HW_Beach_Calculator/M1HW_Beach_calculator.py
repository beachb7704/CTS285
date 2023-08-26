


class Calculations():
    
    def addition(num1, num2):
        answer1 = num1 + num2
        print("result: ", num1, " + ", num2, " = ", answer1)
    
    
    def subtract(num1, num2):
        answer1 = num1 - num2
        print("result: ", num1, " - ", num2, " = ", answer1)
    
    
    def multiply(num1, num2):
        answer1 = num1 * num2
        print("result: ", num1, " * ", num2, " = ", answer1)
    
    
    def divide(num1, num2):
        try:
            answer1 = num1 / num2
            print("result: ", num1, " / ", num2, " = ", answer1)
        #This error will throw an error if you try to divide a number by zero
        except ZeroDivisionError:
            print("You can't divide by zero")
            
            
        