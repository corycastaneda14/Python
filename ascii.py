'''Start Your Python Script:
Open your Python environment and start a new script.
Use a main() function to organize your code.
Prompt for User Input:
Ask the user to enter a single character using input().
Validate the Input:
Ensure the user enters precisely one character.
Use len() to check input length.
Convert to ASCII Value:
Use the built-in function ord() to get the ASCII value.
Example:
ascii_value = ord(user_input)
Display the Result:
Print the ASCII value to the user.
Reverse Lookup:
Prompt the user to enter an ASCII value.
Ensure that the value is between 32 and 127.
Use a try-except block to handle invalid inputs.
Use the built-in function chr() to get the corresponding character.
Example:
character = chr(ascii_input)'''
def main():#Main function
    user_input=input("Enter a single character: ")#Gets user input
    if len(user_input)==1:#Makes sure only one character is entered
        print("Good job")#Validates input
    else:#For wrong inputs
        print("Please enter only one character")#Gives feedback
    ascii_value=ord(user_input)#Gets ASCII value
    print(ascii_value)#Prints ASCII value
    try:#For converting ASCII value
        ascii_input=int(input("Enter an ASCII value between 32 and 127: "))#Gets user input
        if ascii_input >=32 and ascii_input <=127:#Makes sure number is between 32 and 127
            character=chr(ascii_input)#Gets corresponding character
            print("The corresponding character is", character)#Prints corresponding character
        else:#For wrong inputs
            print("Please enter a number between 32 and 127: ")#Gives feedback
    except ValueError:#For wrong inputs
        print("Please enter a number between 32 and 127")#Gives feedback
main()#Runs program