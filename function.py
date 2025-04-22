'''Start with Function Definitions:
Define two functions: square and circle.
Each function should take one parameter (side for square, radius for circle).
Write the square Function:
Calculate the area as side * side and display the result: "The area of the square is [result] square units."
Write the circle Function:
Calculate the area using the formula: area = π * radius * radius. Use 3.14 for π.
Display the result: "The area of the circle is [result] square units."
Test Your Functions:
Call square and circle with sample values.'''
def square(side):#Square formula
    result=side*side#Does calculation
    print(f"The area of the square is {result} square units.")#Prints result

def circle(radius):#Circle formula
    result=3.14*radius*radius#Does calculation
    print(f"The area of the circle is {result} square units. ")#Prints result
square(5)#Runs square function
circle(4)#Runs circle function