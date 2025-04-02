'''Directions:
Accept a numeric grade from the user and display a letter grade. The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F'''
#This program will receive a number and output the corresponding letter grade.

#Get numeric grade
number = int(input("What is your number grade? "))
if number >= 90:
    grade = "A"
elif number >= 80:
    grade = "B"
elif number >= 70:
    grade = "C"
elif number >= 60:
    grade = "D"
else:
    grade = "F"

print("Your letter grade is:", grade)