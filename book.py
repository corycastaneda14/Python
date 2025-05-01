'''Set Up the Main Function: Write your program inside a main function. This is where your while loop will be implemented.
Collect Book Titles: Use a while loop to ask the customer to enter 10 book titles. Store these titles in a list.
Ensure proper capitalization: Use the title function to ensure that the first letter is capitalized before storing it in the list.
Create a Sorted List: Once all titles are collected, save them to a new list named books_sorted. This list should contain the titles in alphabetical order.
Display the Titles: Use a for loop to print each title from the sorted list on a separate line.
Test Your Program: Ensure your program runs correctly and meets all the requirements.
Upload to GitHub: Once tested, upload your program to GitHub.
Submit Your Work: Submit the link to your GitHub repository on Canvas.'''
def main():#Main function
    books=[]
    print("Please enter 10 book titles. ")#Prompts user for books
    while len(books)!=10:#Loop to get book names
        title=input("Please enter a book title: ")#Gets book names
        title=title.title()#Makes book titlecase
        books.append(title)#Puts books in list
        books_sorted=sorted(books)#Sorts books
    print("These are the sorted books: ")#Says the books are sorted
    for book in books_sorted:#Runs printing loop
        print(book)#Prints books
main()#Runs program