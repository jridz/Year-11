from dataclasses import dataclass # Import stuff that the guy used in the video
@dataclass
class employee(): # Initialise the class with each variable type
    surname:str
    name:str
    number:int
    rate:float

employees = [] # Init array

employees.append(employee("Jones", "Kerry", 31532, 7.85)) # Append employee details to array (surname, name, number, and rate)
employees.append(employee("McAllister", "David",	93420,	8.30))
employees.append(employee("Nguyen",	"Tran",	29486,	7.40))
employees.append(employee("Hussein",	"Wasim",	94756,	7.85))
employees.append(employee("Davis",	"Mary",	45820,	8.00))
employees.append(employee("Schmidt",	"Heidi",	61922,	7.60))
# To add more employees, copy an above line and replace it with the applicable data

for i in range(len(employees)): # Loop over all the employees in the array
    x = employees[i] # Assign friendlier label so I can type less
    print(f"Employee #{x.number} {x.name} {x.surname}'s pay rate is " + "${:.2f}".format(x.rate) + "/hour") # Output details in a human friendly format