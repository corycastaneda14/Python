'''In this assignment, you will create a Python program that generates a random number between 1 and 100. Your program should allow the user to guess the number, and provide feedback on how close their guess is to the actual number.
Assignment Objectives:
Use the random module to generate a random number.
Implement a while loop to allow continuous guessing until the correct number is guessed.
Use the abs() function to determine the difference between the guess and the actual number.
Provide feedback based on the proximity of the guess to the actual number:
If the difference is within 5, print "Very Hot".
If the difference is within 15, print "Hot".
If the difference is within 25, print "Cool".
If the difference is more than 25, print "Cold".
Make sure to call the main function!
After completing the program, upload it to your GitHub repository.Import the random module and use it to generate a random number between 1 and 100.
Write a while loop that allows the user to enter a guess for the number.
Inside the loop, use the abs() function to calculate the absolute difference between the guess and the actual number.
Provide feedback based on the computed difference (e.g., "Very Hot" for close guesses).
The loop should continue until the user guesses the correct number.
'''
import random 
def main():#Generate random number
    guess_number=random.randint(1,100)#Range of 1-100
    while True:#Runs loop
        try:
           guess=int(input("Guess a number between 1 and 100: "))
        except ValueError:#For other numbers or words
            print("Please enter a number between 1 and 100: ") 
        if guess==guess_number:#For if guess is correct
            print("You guessed correctly")
        else:#For incorrect guesses
            difference=abs(guess-guess_number)#Gets difference between guess and correct number
            if difference<=5:#Gives feedback
                print("Very Hot")
            elif difference<=15:#Gives feedback
                print("Hot")
            elif difference<=25:#Gives feedback
                print("Cool")
            elif difference<=26:#Gives feedback
                print("Cold")
main()#Runs program