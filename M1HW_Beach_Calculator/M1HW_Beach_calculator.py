


class Calculations():
    '''
     This function performs addition, subtraction, multiplication, and division. 
     
    inputs: numbers selected by the user
    outputs: will return the calculation that the user selected along with the integers input.
    ''' 
    
    # Will take the numbers selected, add them together then display the function.
    #====================#
    # Addition Function  #
    #====================#
    
    def addition(num1, num2):
        answer1 = num1 + num2
        print("result: ", num1, " + ", num2, " = ", answer1)
    
    
    # Will take the numbers selected, add them together then display the function.
    #====================#
    # Subtraction Function  #
    #====================#
    
    def subtract(num1, num2):
        answer1 = num1 - num2
        print("result: ", num1, " - ", num2, " = ", answer1)
    
    
    # Will take the numbers selected, add them together then display the function.
    #==========================#
    # Multiplicaiton Function  #
    #==========================#
    
    def multiply(num1, num2):
        answer1 = num1 * num2
        print("result: ", num1, " * ", num2, " = ", answer1)
    
    
    # Will take the numbers selected, add them together then display the function.
    #====================#
    # Division Function  #
    #====================#
    
    def divide(num1, num2):
        try:
            answer1 = num1 / num2
            print("result: ", num1, " / ", num2, " = ", answer1)
        #This error will throw an error if you try to divide a number by zero
        except ZeroDivisionError:
            print("You can't divide by zero")
            
            
        