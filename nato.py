'''Create the NATO Phonetic Alphabet Dictionary:
Construct a dictionary in Python named nato_alphabet, where each key is a letter, and its value is the corresponding NATO phonetic term.
Develop the Spelling Program:
Write a function to prompt the user for a word and iterate through each letter to find and print the NATO phonetic term.
Incorporate a Main Function:
Encapsulate your logic within a main() function for organization.
Test Your Program:
Test the program with various inputs, ensuring it works as expected.'''
nato_alphabet={#Dictionary
    "A":"Alfa",
    "B":"Bravo",
    "C":"Charlie",
    "D":"Delta",
    "E":"Echo",
    "F":"Foxtrot",
    "G":"Golf",
    "H":"Hotel",
    "I":"India",
    "J":"Juliett",
    "K":"Kilo",
    "L":"Lima",
    "M":"Mike",
    "N":"November",
    "O":"Oscar",
    "P":"Papa",
    "Q":"Quebec",
    "R":"Romeo",
    "S":"Sierra",
    "T":"Tango",
    "U":"Uniform",
    "V":"Victor",
    "W":"Whiskey",
    "X":"Xray",
    "Y":"Yankee",
    "Z":"Zulu"}
def main():
    word = input("Enter a word to receive the NATO Phonetic spelling: ")#Prompts user for input
    for letter in word:
        letter=letter.upper()#Makes the letters uppercase.
        if letter in nato_alphabet:#Starts process of finding matching word
            print(nato_alphabet[letter])#Prints matching words
        else:
            print("This is not in the alphabet")#This is for numbers or other stuff.
main()#Runs program