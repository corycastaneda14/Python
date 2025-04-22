'''Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content.
Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc.
Write the Function:
Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
Use f-strings to incorporate these parameters into the song's lyrics.
Ensure the function prints the customized song lyrics.
Collect User Input:
Write code to collect user input for each of the 8 variables.
Use clear and descriptive prompts to guide the user.
Call the Function:
Call the custom_song function with the user inputs as named arguments.
Ensure the order of arguments matches the parameters in your function definition.'''
def custom_song():#Function
    print("Roar -Katy Perry (Madlib Version)")#Introduces the song
    verb1=input("Enter an action verb: ")#Gets a variable
    emotion1=input("Enter an emotion: ")#Gets a variable
    verb2=input("Enter a past tense verb: ")#Gets a variable
    noun1=input("Enter a noun: ")#Gets a variable
    verb3=input("Enter a verb: ")#Gets a variable
    verb4=input("Enter a verb with a -ing ending: ")#Gets a variable
    noun2=input("Enter a noun: ")#Gets a variable
    adjective1=input("Enter an adjective: ")#Gets a variable
    print(f"I used to bite my tongue and {verb1} my breath")#Prints lyric with variable
    print(f"{emotion1} to rock the boat and make a mess")#Prints lyric with variable
    print(f"So I {verb2} quietly, agreed politely")#Prints lyric with variable
    print(f"I guess that I forgot I had a {noun1}")#Prints lyric with variable
    print(f"I let you {verb3} me past the breaking point")#Prints lyric with variable
    print(f"I stood for {verb4} so I fell for everything")#Prints lyric with variable
    print(f"You held me down but I got {noun2}")#Prints lyric with variable
    print(f"Already brushing {adjective1} the dust")#Prints lyric with variable
custom_song()#Runs the program