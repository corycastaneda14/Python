'''Write the program "99 Bottles of Beer on the Wall" using a while loop. Be mindful to change the word 'bottles' to 'bottle' when down to the last one. You must do the full 99 bottles; the sample shows the last 3 verses.'''
count = 99  # Starting with 99 bottles

while count > 0:
    if count == 1:
        print(count, "bottle of beer on the wall")
        print(count, "bottle of beer")
        print("Take it down, pass it around")
        print("No bottles of beer on the wall!\n")
    elif count == 2:
        print(count, "bottles of beer on the wall")
        print(count, "bottles of beer")
        print("Take one down, pass it around")
        print(count - 1, "bottle of beer on the wall!\n")
    else:
        print(count, "bottles of beer on the wall")
        print(count, "bottles of beer")
        print("Take one down, pass it around")
        print(count - 1, "bottles of beer on the wall!\n")
    
    count -= 1  # Decrement count

