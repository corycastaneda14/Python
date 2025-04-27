'''Start by defining a function named factorial that takes one parameter, n, representing the number you're calculating the factorial for.
In your factorial function, first define the base case: n == 1 or n == 0, where the factorial is 1.
For the recursive step, return n * factorial(n-1) if n > 1.
Prompt the user for a non-negative integer and call factorial, printing the result.'''
def factorial(n):#Factorial function
    if n==1 or n==0:#For if you enter 0 or 1.
        return 1#Gives this value
    else:#For all other values
        return n*factorial(n-1)#Formula used 
user_number=int(input("Please enter a non-negative integer: "))#Gets user input
result=factorial(user_number)#Call factorial with user number.
print(f"The factorial of {user_number} is {result}.")#Prints result

