'''Create a list representing 20 seats, numbered 1 to 20.
Display the list of available seats to the customer.
Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.
Remove the selected seat from the list of available seats and display the updated list.
If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
Ensure the program gracefully handles all scenarios and is user-friendly.'''

seats_list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]#List of available seats
print("Here are the available seats:", seats_list)#Gives seat options
print("Please select a seat by entering its number. Entering 0 ends the purchase process.")#Tells you what to do
while True:
    user_input = int(input("Please select a seat number: "))#Enter your number to start

    if user_input == 0:
        print("The purchasing process has ended.")#This is to end the program
        break #Needed to stop the program. It would not stop without this
    elif user_input in seats_list:
        seats_list.remove(user_input)#Removes seat once you select it.
        print(f"{user_input} has been selected.")#Prints seat you selected
        print("Here are the available seats:", seats_list)#New list of available seats
    else:
        print("This seat is unavailable.")#For all other numbers