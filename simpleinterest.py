'''Write a Python function named calculate_interest that computes and returns simple interest based on given parameters.A main function should control the logic of the program
Create and call a function should be named calculate_interest.
It should take three parameters that you get from the user:
principal - The initial amount.
rate - The annual interest rate (percentage).
time - The investment duration in years.
Use the return keyword to send back the computed interest to a variable in the main function.
Print the result using formatted strings in the main function.'''

def main():
    principal = float(input("What is the principal amount? "))
    rate = float(input("What is the annual interest rate? "))
    time= float(input("What is the duration of the investment? "))
    interest= calculate_interest(principal,rate,time)
    print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")
def calculate_interest(principal,rate,time):
    return (principal*rate*time)/100
main()