''' Create a BMI calculator that takes a user's weight and height, calculates their BMI, and categorizes it as underweight, normal weight, overweight, or obese.

Requirements:
Global Variables:
Conversion constants for weight (1 lb = 0.453592 kg) and height (1 in = 0.0254 m).
Main Function:
Prompt the user for their weight in pounds and height in inches.
Convert the inputs to metric units using global conversion constants.
Calculate BMI using the formula bmi = weight / (height * height).
Determine the BMI category based on standard ranges.
Display the BMI value and category.
Commenting:
Include comments to explain key parts of the code.'''
pounds_tokg= 0.453592#Pounds to kg
in_tom=0.0254#Inches to m
def main():
    weight_lbs=float(input("Enter your weight in lbs. "))#Gets weight
    height_in=float(input("Enter your height in inches. "))#Gets height
    weight_kg= weight_lbs*pounds_tokg#conversion
    height_m=height_in*in_tom#Conversion
    bmi=weight_kg/(height_m*height_m)#Calculates BMI
    if bmi<18.5:#Determines category you fall in
        category="Underweight"
    elif 18.5<=bmi<24.9:
        category="Normal"
    elif 25<= bmi<29.9:
        category="Overweight"
    elif 30<= bmi<39.9:
        category="Obese"
    else:
        category="Severely Obese"
    print(f"Your BMI is: {bmi:.2f}")#Prints BMI
    print(f"Category: {category}")#Prints category
main()#Runs program

