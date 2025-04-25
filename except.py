'''Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
Identify Potential Errors: Consider errors that might occur with non-numeric input.
Add Exception Handling: Implement try and except blocks to catch a ValueError. Handle incorrect data types with an error message.
Test Your Code: Ensure the exception handling works correctly with various inputs.
GitHub Upload: Upload your py file to GitHub and hand in the link'''
# Simple Python program to calculate the square of a number
def square_number():  # Main function
    try:
        number = input("Enter a number to square: ")  # Gets user's number
        squared_number = int(number) ** 2  # Performs calculation
        print(f"The square of {number} is {squared_number}.")  # Prints result
    except ValueError:#Added this for non-numbers.
        print("Please enter a whole number.")  # Error message for invalid input

square_number()