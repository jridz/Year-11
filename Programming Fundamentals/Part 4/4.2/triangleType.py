def checkEquilateral(a, b, c):
    isEquilateral = False
    if a == b == c:
        isEquilateral = True
    return isEquilateral

def checkIsosceles(a, b, c):
    isIsosceles = False
    if a == b or a == c or b == c:
        isIsosceles = True
    return isIsosceles

def goAgain():
    again = False
    askResponse = str(input("Would you like to go again? Type \"y\" for yes and \"n\" for no): "))
    if askResponse == "y":
        again = True
    return again

repeat = True
while repeat == True:
    side_A = float(input("What is the length of the first side of the triangle? "))
    side_B = float(input("What is the length of the second side of the triangle? "))
    side_C = float(input("What is the length of the third side of the triangle? "))

    equilateral = checkEquilateral(side_A, side_B, side_C)
    if equilateral:
        triangleType = "Equilateral"
    else:
        isosceles = checkIsosceles(side_A, side_B, side_C)
        if isosceles:
            triangleType = "Isosceles"
        else: 
            triangleType = "Scalene"
    print("Triangle type is " + triangleType)
    repeat = goAgain()