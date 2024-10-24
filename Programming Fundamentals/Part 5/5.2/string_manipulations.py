baseString = str(input("Enter a string to modify: ")) # The base string

operation = int(input("Select an operation to do on the string:\n(1) Uppercase\n(2) Lowercase\n(3) Count\n")) # How the user wants to modify the string

if operation == 1:
    print(baseString.upper()) # Prints out string in uppercase
elif operation == 2:
    print(baseString.lower()) # Prints out string in lowercase
elif operation == 3:
    character = input("Character to count: ") # Gets character(s) to count
    print("There are " + str(baseString.count(character)) + " instances of \"" + character + "\" in the string.") # Puts counted character in string and prints string
else:
    print("Please select a valid operation (1, 2, 3)") # Error if operation invalid