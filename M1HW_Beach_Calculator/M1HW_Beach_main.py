#// CTS 285
#// M1HW
#// Brenda Beach
#// August 21, 2023
#As a programmer I want to create programs so that I can input student informaiton into our class database easier
# than using Microsoft Access as our database.



# Import all of the other modules needed to run inside this module
#=============#
# Imports     #
#=============#
from M1HW_Beach_user_choice import *



#=============#
def main():
#=============#
        """ 
    This function starts the program and looks into new module to show main menu to the user. 
    
    inputs: none
    outputs: sent request to user_choice module and displays main menu
        """
        
        user_input.start_menu()
        


if __name__ == '__main__':
        main()