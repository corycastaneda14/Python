'''Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.'''
names = []#Get names
for i in range(5):#Limits to 5 names
    name= input(f"Enter name {i+1}: ")#Takes users name
    names.append(name)#Adds name to list
print("You entered:", names)#Display the given names
n = len(names)#Makes the n variable the total number of names.
for i in range(n):#This makes it loop
    for j in range(0, n-i-1):#Compares the names next to each other in the bubble
        if names[j] > names[j+1]:#This swaps the names if they need to be.
            names[j], names[j+1] = names[j+1], names[j]#Takes name and the one next to it and switches them.
print("Here are the sorted names" ,names)#Prints sorted names
names.reverse()#Reverses names
print("Here are the names sorted backwards" ,names)#Prints reversed names
