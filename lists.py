'''Create a List: Start by creating a list named days that includes all seven days of the week.
Initialize an Empty List: Create an empty list called steps to store the number of steps taken each day.
User Input: Using a loop, ask the user to enter the number of steps they took for each day.
Store Steps: Append the user's input to the steps list.
Display Daily Steps: Show the user the steps recorded for each day.
Total Steps: Calculate and display the total number of steps taken in the week.
Average Steps: Calculate and display the average steps.'''
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]#These are the days
steps = []#Empty list to hold steps given.

for day in days:#Question loop
    user_input = int(input(f"How many steps did you take on {day}? "))#Gets the steps each day
    steps.append(user_input)#Adds give number to empty list.

print("The steps for each day are:", steps)#Prints confirmation of numbers given
total= sum(steps)#Adds all the numbers
print("The total number of steps taken is",total)#Prints total
average=sum(steps)/7 #Divides total number of steps by the number of days in a week.
print("The average amount of steps taken in a day are", average)#Prints average amount of steps each day.
