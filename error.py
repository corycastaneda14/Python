'''Write a short interactive Python program of your choice that uses try and except to catch and respond to at least two specific exceptions. Your program should:
Include a main() function.
Use try and except to catch specific errors like ValueError or ZeroDivisionError.
Provide helpful messages when errors occur.
Do something meaningful or fun—be creative! You could build a number guessing game, a basic calculator, or even a simple quiz with input validation.'''
def main():#Main function
    print("Physics Speed Formula (speed=distance/time)")#Introduces formula
    try:
        d=float(input("Please enter the distance in miles: "))#Gets distance
        t=float(input("Please enter the time in hours: "))#Gets time
        s=d/t#Does math
        print(f"The speed was: {s} miles per hour. ")#Prints result
        
    except ValueError:#For non-numbers
        print("Please enter a number. ")#Gives feedback
    except ZeroDivisionError:#For when time is 0
        print("Please enter a number. The time given is not possible ")#Gives feedback
main()#Runs program

