'''Create a tuple named programming_classes with these classes: 'Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals'.
Write a program that uses a for loop to print each class in the tuple.
Use the len function to print how many courses are in the tuple.
Make sure to use a main function for this program.'''
def main():#Main function
    programming_classes=('Intro to Python', 'Advanced Python','Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')#Contains tuple

    for item in programming_classes:#Loop of the classes
     print(item)#Prints class names
    print("There are", len(programming_classes),"programming classes.")#Prints number of classes
main()#Runs program