import random # imports Python random numbers library

# Check if generated number is unique
def CheckUnique (num, array):
    unique = True
    for number in array:
        if num == number:
            unique = False
            break # stop looking, leave the for loop
    return unique

# How many numbers?
limit = int(input("How many random numbers do you want? ")) # needs to be an integer

# Initialise array
RandomNumbers = []
RandomNum = random.randint (1,100)
RandomNumbers.append(RandomNum)

# Generate more numbers
for index in range (1, limit): 
    unique = False # set unique flag to false after each new number added to list
    while not unique:
        RandomNum = random.randint (1,100) # generates a random integer between 1 and 100, inc
        unique = CheckUnique(RandomNum, RandomNumbers)
    RandomNumbers.append (RandomNum) # add unique number to list

# Sort the array
RandomNumbers.sort()

# Print the numbers
print(RandomNumbers)