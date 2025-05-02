'''Set up your program in a main() function.
Create a Python program that asks the user to input a password.
Ensure the password meets the following criteria:
Between 8 to 20 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Includes at least one number.
Includes at least one symbol from the set: !@#$%&*.
Use a while loop to keep asking for the password until all criteria are met.
Once a valid password is entered, prompt the user to enter it again for confirmation.
Use try-except blocks to handle any errors or exceptions that occur.
If the second password entry matches the first, display a success message. Otherwise, prompt the user to start the process again.'''
def main():#Main function
    print("Password must be between 8 and 20 characters, contain at least 1 uppercase and 1 lowercase letter, 1 number, and 1 symbol ")
    special_ch="!","@","#","$","%","&","*",#List of special characters
    while True:#Runs loop
        password=input("Please enter a password: ")#Prompts user for password
        if len(password)<8 or len(password)>20:#Makes sure length is good
            print("Please keep it between 8 and 20 characters.")#Gives feedback
            continue#Keeps program going
        has_upper=any(char.isupper() for char in password)#Checks for upper
        has_lower=any(char.islower() for char in password)#Checks for lower
        has_digit=any(char.isdigit() for char in password)#Checks for number
        has_special=any(char in special_ch for char in password)#Checks for special character
        if not (has_upper and has_lower and has_digit and has_special):#Makes sure you fulfill requirements
            print("Password must follow the parameters.")#Gives feedback
    
        confirmation=input("Please enter password again to confirm: ")#Prompts you to confirm password
        if confirmation ==password:#Checks password
            print("Password is confirmed")#Gives feedback
        else: 
            print("The passwords don't match")#Gives feedback
main()#Runs program