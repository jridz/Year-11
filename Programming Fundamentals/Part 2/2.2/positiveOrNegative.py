print()
try:
    number = int(input("Enter a whole number: "))
    print()
    if number > 0:
        if number%2 == 0:
            print(str(number) + " is a positive even number")
        else:
            print(str(number) + " is a positive odd number")
    else:
        print(str(number) + " is a negative number or zero")
except ValueError:
    print("Error: Enter whole numbers only.")