'''Write a Python program that uses if-else statements and:

Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward and user-friendly.
'''
age=int(input("What is your age? ")) #Gets number to determine how old you are.

if age>= 16:
    print("You are old enough to drive.")
elif age<16:
    print("You are not old enough to drive") #The code up to here is to determine if you can drive
if age >= 18:
    print("You are old enough to vote.")
elif age<18:
    print("You are not old enough to vote") #The code up to here is to determine if you can vote.
if age>= 21:
    print("You are old enough to buy alcohol.")
elif age<21:
    print("You are not old enough to buy alcohol") #The code up to here is to determine if you can buy alcohol.
if age>= 65:
    print("You are eligible for the senior discount.")
elif age <65:
    print("You are not old enough for the senior discount.") #The code up to here is to determine if you are eligible for the senior discount.
