class Animal:
    def __init__(self, name, gender, diet, cold_blooded):
        self.name = name
        self.gender = gender
        self.diet = diet
        self.cold_blooded = cold_blooded

    def eat(self):
        print(self.name + " is eating " + self.diet)


class Frog(Animal):
    def __init__(self, name, gender, color, isPoisonous):
        super().__init__(name, gender, diet="insects", cold_blooded=True)
        self.color = color
        self.isPoisonous = isPoisonous

    def hop(self):
        print(self.name + ": BOING!")


class Horse(Animal):
    def __init__(self, name, gender, color):
        super().__init__(name, gender, diet="grass", cold_blooded=False)
        self.color = color

    def gallop(self, times):
        if times < 1:
            print("You can't gallop less than once.")
            return
        clops = ""
        for i in range(times):
            clops = clops + "CLOP "
        print(self.name, ":", clops)


class Snake(Animal):
    def __init__(self, name, gender, pattern):
        super().__init__(name, gender, diet="mice", cold_blooded=True)
        self.pattern = pattern

    def hiss(self, length):
        if length < 1:
            print("You can't hiss less than one.")
            return
        hiss = "HI"
        for i in range(length):
            hiss = hiss + "S"
        print(self.name + ": " + hiss + "~")
