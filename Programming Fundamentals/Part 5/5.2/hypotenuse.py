side1 = float(input("Triangle Side 1 Length: ")) # Gets side lengths as floats
side2 = float(input("Triangle Side 2 Length: "))

hypotenuse = (side1**2 + side2**2)**0.5 # Uses the pythagorean theorem to calculate the hypotenuse
hypotenuse = round(hypotenuse, 1) # Rounds hypotenuse to 1 d.p.

url = "https://www.calculator.net/triangle-calculator.html?vc=&vx=" + str(side1) + "&vy=" + str(side2) + "&va=&vz=" + str(hypotenuse) + "&vb=&angleunits=d&x=Calculate" # Base unpopulated URL
print("The hypotenuse is " + str(hypotenuse) + " (rounded to 1 decimal place.)") # Prints hypotenuse

visualise = input("Would you like to visualise your triangle? (y/N) ") # Asks if user wants to visualise
if visualise == "y": print("Visualise your triangle here: " + url) # Prints populated URL to visualiser
else: exit() # If not, exit