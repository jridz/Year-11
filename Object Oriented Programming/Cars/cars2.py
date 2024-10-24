class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"The engine of {self.make} {self.model} is now running.")

    def rev_engine(self):
        print(f"{self.make} {self.model} is revving the engine.")

    def change_gear(self, gear):
        print(f"{self.make} {self.model} is changing gear to {gear}.")


# Creating objects
my_car = Car("Toyota", "Corolla")
your_car = Car("Honda", "Civic")

# Sending messages (method calls)
my_car.start_engine()
your_car.start_engine()

my_car.rev_engine()
your_car.rev_engine()

my_car.change_gear(3)
your_car.change_gear(2)
