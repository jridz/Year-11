# Program to input and display a list of friends
# initialisation

# declare array
Friends = [] # creates an empty list/array called Friends

# initialise loop termination value
Continue = "y"

# get the names
while Continue != "n": # Python doesn't have a post-test loop
    name = input("Type in a friends name: ")
    Friends.append(name) # add entered name to the end of the list 
    Continue = input("Do you want to enter another name? (y/n) ")

# display the list of names
print("You have " + str(len(Friends)) + " friends.")
print("Their names are:")

# Sort array
Friends.sort()

for name in Friends: # goes through the list, printing each name on a new line 
    print(name)