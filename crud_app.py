'''Complete the read, delete, and update functions following similar patterns. Use inputs to search for entries and modify the list of customers accordingly.
By the end of this lesson, you should be able to create, read, update, and delete entries in a text-based application. Test each function thoroughly to ensure they work as expected.'''
def main_menu():
    print("Menu:")
    while True:
        try:
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))# Ask user for a choice
            if 1 <= choice <= 5:# Validate input is in range
                return choice# Return the valid choice
            else:
                print("That is not a valid number. Try again.")#Invalid range
        except ValueError:
            print("That is not a valid number. Try again.")#If input isn't a number


def check():
    try:
        file = open("customer_list.txt", 'r')#Try opening the file in read mode
        lines = file.readlines()#Read all lines into a list
        file.close()#Close the file
        return lines#Return the list of customers
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")#If file doesn't exist
        return []#Return empty list


def save(output):
    file = open("customer_list.txt", 'w')#Open file in write mode (overwrite)
    for line in output:
        file.write(line)#Write each line to the file
    file.close()  # Close the file
    print("File updated.")  # Confirm save


def create():
    customer = check()  # Load customer data
    fname = input("Please enter the customer's first name: ")  # Get first name
    lname = input("Please enter the customer's last name: ")  # Get last name
    phone = input("Please enter the customer's phone: ")  # Get phone number
    email = input("Please enter the customer's email: ")  # Get email
    entry = f"{fname}, {lname}, {phone}, {email}\n"  # Format entry
    customer.append(entry)  # Add entry to the list
    save(customer)  # Save updated list


def read():
    customer = check()  # Load customer data
    search = input("Enter the last name to search: ").strip().title()  # Ask for last name
    found = False  # Flag to track if we find a match
    for line in customer:
        if line.strip() == "":
            continue  # Skip empty lines
        parts = line.strip().split(", ")  # Split line into parts
        if len(parts) >= 2 and parts[1].title() == search:  # Compare last name
            print("Found:", line.strip())  # Print matching entry
            found = True  # Set flag
    if not found:
        print("No entry found with that last name.")  # If not found


def update():
    customer = check()  # Load customer data
    search = input("Enter the last name of the entry to update: ").strip().title()  # Get last name to update
    updated_list = []  # New list to hold updated data
    found = False  # Flag to track if we found a match

    for line in customer:
        parts = line.strip().split(", ")  # Split the line
        if len(parts) >= 2 and parts[1].title() == search:  # Match last name
            print("Current entry:", line.strip())  # Show current info
            fname = input("Enter new first name: ")  # Get updated info
            lname = input("Enter new last name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            updated_line = f"{fname}, {lname}, {phone}, {email}\n"  # Create new entry
            updated_list.append(updated_line)  # Add updated line
            found = True  # Set flag
        else:
            updated_list.append(line)  # Keep original if not matched

    if found:
        save(updated_list)  # Save updated list
    else:
        print("No matching entry found.")  # If no match found


def delete():
    customer = check()  # Load data
    search = input("Enter the last name of the entry to delete: ").strip().title()  # Get name to delete
    updated_list = []  # New list to hold remaining data
    found = False  # Flag to track deletion

    for line in customer:
        parts = line.strip().split(", ")  # Split line
        if len(parts) >= 2 and parts[1].title() == search:  # If match
            print("Deleting:", line.strip())  # Show what’s being deleted
            found = True  # Set flag
            continue  # Skip adding this entry
        updated_list.append(line)  # Keep unmatched entries

    if found:
        save(updated_list)  # Save updated list
    else:
        print("No matching entry found.")  # No match to delete


def main():
    while True:
        choice = main_menu()  # Show menu and get user choice
        if choice == 1:
            create()  # Create new entry
        elif choice == 2:
            read()  # Search for an entry
        elif choice == 3:
            update()  # Update an existing entry
        elif choice == 4:
            delete()  # Delete an entry
        elif choice == 5:
            print("Goodbye!")  # Exit program
            break


main()  # Run the program

