import turtle
import random


turtle.colormode(255)
turt = turtle.Turtle()
turt.speed(100)
turt.color("green")
turt_this = turtle.Turtle()


turt.pendown()
for i in range(10):
    length = random.randint(20, 50)
    angle = random.randint(-15, 15)
    flipAngle = angle
    turt.right(angle)
    turt.forward(length)
    turt_this.penup()
    turt_this.right(angle)
    turt_this.forward(length)
    turt_this.pendown()
    turt_this.right(flipAngle)
    turt_this.forward(length)
    turt_this.penup()
    turt_this.left(flipAngle)
    turt_this.backward(length)
turtle.done()

