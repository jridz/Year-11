hours = float(input("How many hours of work?\n Hours: ")) # Gets hours and sets response to variable
hourlyRate = float(input("What is your hourly rate? ($/hour)\n $")) # Gets hourly rate and sets response to variable
grossPay = format(hours * hourlyRate, ",.2f") # Calculates gross pay by multiplying hourly rate by hours and formats as currency
print("Your gross pay is $" + str(grossPay) + " for " + str(hours) + " hour(s) of work at $" + str(hourlyRate) + "/hour.") # Returns the users Gross Pay as well as hours and rate as a human readable output