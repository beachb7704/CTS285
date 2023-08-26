#// CTS 285
#// M1T1
#// Brenda Beach
#// August 21, 2023

#This will print my welcome message and name
def user_name():
    print("Hello professor, my name is Brenda Beach.")

#This will print language learned on multiple lines
def languages():
    print('I am not currently learning a language this semester but I am taking NOS-120-0901 Linux/UNIX Single User.\n' 
          'I  have already taken Java and Python 1 and 2. My preferred coding language is Python.')

#This will print additional info about me
def additional_info():
    print("I am an Army veteran with 11 years of service. I was Signal Corps my entire career.\n"
          "I have a daughter who is 23 years old and is in Culinary School online. I am currently employed with Lockheed Martin,\n"
          "and I am what they call a SASMO (Sustainment Automation Support Management Office). We work on the computer \n"
          "systems that soldiers use to order parts, maintain their trucks, and weapon systems. I also work on the sattelite \n"
          "systems they use when they deploy so they can have internet access to the program they have to use. \n"
          "I am also an instructor and teach the soldiers the maintenance portion of the program that they have to use. \n"
          "In my spare time, I like to create digital embroidery patterns, then stitch them out on my embroidery machine, \n"
          "as well as play video games on my switch.")


#This will run the functions in a specific order
def main():
    user_name()
    languages()
    additional_info()



if __name__ == '__main__':
    main()