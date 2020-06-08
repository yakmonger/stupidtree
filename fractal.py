import turtle
turtle.speed(0)
min = 5

import random


def drawfractal(length, short, angle):
    if length > min:
        angle = random.randint(20, 50)
        turtle.forward(length)
        newlong = length - short
        turtle.right(angle)
        drawfractal(newlong, short, angle)
        turtle.left(angle * 2)
        drawfractal(newlong, short, angle)
        turtle.right(angle)
        turtle.backward(length)
        
        rand = random.randint(1, 10)

turtle.hideturtle()
turtle.setheading(90)
turtle.color('blue')
drawfractal(50, 5, 20)
turtle.mainloop()
turtle.done()
        

