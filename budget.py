# Requirements:
#     Design a Python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
#     Housing (rent or mortgage)
#     Utilities
#     Groceries
#     Transportation
#     Health Care
#     Personal Care
#     Clothing
#     Debt
#     Calculate the percentage of the total budget spent in each category.
#     Display the results in a user-friendly format using f-strings.
#     Ensure your code is well-commented to explain the functionality of different sections.
# '''

# # Get input from user

budget = float(input("Please enter your net monthly income for the budget: "))
housing = float(input(
   "Please enter your housing costs (rent or mortgage plus HOA if you have it: "))
utilities = float(input("Please enter your monthly utilities cost: "))
groceries = float(input("Please enter your monthly grocery costs: "))
transportation = float(input("Please enter your monthly transportation costs. This may include car payment and gas: "))
healthcare = float(input("Please enter your monthly health expenses such as prescriptions or insurance: "))
personalcare = float(input("Please enter the cost of your personal items: "))
clothing = float(input("Please enter your monthly cost for clothing. This can include fees if you use a public laundry service: "))
debt = float(input("Please enter your monthly debt payment: "))

# # Perform calculations
housing_percent = (housing*100)/budget
utilities_percent = (utilities*100)/budget
groceries_percent = (groceries*100)/budget
transportation_percent = (transportation*100)/budget
healthcare_percent = (healthcare*100)/budget
personalcare_percent = (personalcare*100)/budget
clothing_percent = (clothing*100)/budget
debt_percent = (debt*100)/budget
# Output
print()
print()
print()
print()# This is to create some blank space in the terminal so the results are neater.
print(f"Your housing is %{housing_percent:.1f} of your monthly budget.")
print(f"Your utilities are %{utilities_percent:.1f} of your monthly budget.")
print(f"Your groceries are %{groceries_percent:.1f} of your monthly budget.")
print(f"Your transportation is %{transportation_percent:.1f} of your monthly budget.")
print(f"Your healthcare is %{healthcare_percent:.1f} of your monthly budget.")
print(f"Your personal care is %{personalcare_percent:.1f} of your monthly budget.")
print(f"Your clothing is %{clothing_percent:.1f} of your monthly budget.")
print(f"Your debt is %{debt_percent:.1f} of your monthly budget.")