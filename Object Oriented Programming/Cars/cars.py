class Car:
    def __init__(self, make, model, year, color):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color

    # Getters
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    # Setters
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def drive(self):
        print("This " + self.get_model() + " is driving.")

    def stop(self):
        print("This " + self.get_model() + " is stopped.")


class ElectricCar(Car):
    def __init__(self, make, model, year, color, batteryCapacity, currentCharge):
        super().__init__(make, model, year, color)
        self.__battery_capacity = batteryCapacity
        self.__current_charge = currentCharge

    def get_battery_capacity(self):
        return self.__battery_capacity

    def get_current_charge(self):
        return self.__current_charge

    def set_battery_capacity(self, batteryCapacity):
        self.__battery_capacity = batteryCapacity

    def recharge(self, charge):
        if self.__current_charge + charge > self.__battery_capacity:
            print("You can't charge the battery past its capacity.")
            return
        else:
            self.__current_charge = self.__current_charge + charge
            print("The battery is now at " + str(self.__current_charge) + "/" + str(self.__battery_capacity) + " charge.")
            return


class PetrolCar(Car):
    def __init__(self, make, model, year, color, fuelCapacity, currentFuel):
        super().__init__(make, model, year, color)
        self.__fuel_capacity = fuelCapacity
        self.__current_fuel = currentFuel

    def get_fuel_capacity(self):
        return self.__fuel_capacity

    def refuel(self, fuel):
        if self.__current_fuel + fuel > self.__fuel_capacity:
            print("You can't refuel the tank past its capacity.")
            return
        else:
            self.__current_fuel = self.__current_fuel + fuel
            print("The tank is now at " + str(self.__current_fuel) + "/" + str(self.__fuel_capacity) + " fuel.")
            return


car_1 = PetrolCar("Toyota", "Corolla", 2015, "Red", 50, 20)
car_2 = ElectricCar("Tesla", "Model S", 2018, "Black", 100, 50)

print(car_1.get_make())
print(car_1.get_model())
print(car_1.get_year())
print(car_1.get_color())

print(car_2.get_make())
print(car_2.get_model())
print(car_2.get_year())
print(car_2.get_color())

car_1.refuel(40)
car_1.drive()
car_1.stop()

car_2.recharge(50)
car_2.drive()
car_2.stop()
