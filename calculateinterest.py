'''Define the function calculate_interest with appropriate parameters.
Apply the formula to calculate the simple interest.
Return the calculated interest.
Print the result using an f-string:
Simple Interest = (Principal Amount × Rate of Interest × Time) / 100
'''
#This section is to get the user input for the amounts needed to calculate the interest
principal = float(input("Enter the principal amount:"))
rate = float(input("Enter the interest rate:"))
time = float(input("Enter the time in years:"))
calculate_interest = (principal, rate,time)
interest = principal * rate * time

#This shows the result for the interest
print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")