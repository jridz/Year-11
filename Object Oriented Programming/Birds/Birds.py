class Bird:
    # Initialize the bird's name
    def __init__(self, name):
        self.__name__ = name

    # Method to make a generic bird sound
    def makeSound(self):
        print("Chirp")


class Duck(Bird):
    # Override the makeSound to make a duck sound
    def makeSound(self):
        print("Quack")


class Crow(Bird):
    # Override the makeSound to make a crow sound
    def makeSound(self):
        print("Caw")


class Canary(Bird):
    # Override the makeSound to make a canary sound
    def makeSound(self):
        print("Tweet")


# Create an array of different birds
birdArray = [Bird("bird"), Duck("duck"), Crow("crow"), Canary("canary")]

# Iterate through the array and call the makeSound method for each bird
for bird in birdArray:
    bird.makeSound()
