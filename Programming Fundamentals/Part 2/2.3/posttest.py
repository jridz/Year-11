while True:
   num1 = float(input("Enter the first number: "))
   if num1 < 0: break
   num2 = float(input("Enter the second number: "))
   average = (num1 + num2)/2
   print("The average is: " + str(average))