# Imports
from turtle import *
from random import randint

penup()
goto(-140, 140)
pendown()
speed(0)

# Track
for step in range(20):
    write(step)
    right(90)
    forward(180)
    penup()
    backward(180)
    left(90)
    forward(20)
    pendown()

# Turtles
leonardo = Turtle()
michelangelo = Turtle()
donatello = Turtle()
raphael = Turtle()

# Colors
leonardo.color('blue')
michelangelo.color('orange')
donatello.color('purple')
raphael.color('red')

# Shapes
leonardo.shape('turtle')
michelangelo.shape('turtle')
donatello.shape('turtle')
raphael.shape('turtle')

# Positions
leonardo.penup()
leonardo.goto(-160, 100)
leonardo.pendown()

michelangelo.penup()
michelangelo.goto(-160, 70)
michelangelo.pendown()

donatello.penup()
donatello.goto(-160, 40)
donatello.pendown()

raphael.penup()
raphael.goto(-160, 10)
raphael.pendown()

for movement in range(100):
    leonardo.forward(randint(1, 5))
    michelangelo.forward(randint(1, 5))
    donatello.forward(randint(1, 5))
    raphael.forward(randint(1, 5))
done()
