'''Start by asking the user to input two distinct integers. 
implement six different logical comparisons using the input integers. Include two examples for each of the following operators:
and
or
not
Print the logical statement and its result for each comparison.'''
num1= float(input("Please enter your first number: "))
num2= float(input("Please enter your second number: "))
if num1>0 and num2 >0:#First AND
    print("Both numbers are greater than 0.")
else:
    print("At least on number is not greater than 0.")
if num1<20 and num2<20:#Second AND
    print("At least one number is less than 20.")
else:
    print("At least one number is greater than 20.")

if num1%2 ==0 or num2%2 ==0:#First OR
    print("One of the numbers are even.")
else:
    print("Neither of the numbers are even.")
if num1>=50 or num2>=50:#Second OR
    print("At least one of the numbers rounds up to 100.")
else:
    print("Both numbers would round down to 0.")

if not num1==num2:#First NOT
    print("The numbers are not equal.")
else: 
    print("The numbers are equal.")
if not num1<0 or num2<0:#Second NOT
    print("Neither of the numbers are negative")
else:
    print("At least one of the numbers are negative.")