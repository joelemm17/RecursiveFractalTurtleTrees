
import turtle
import random
import math


height = 1920
width = 1080
turtle.setup(height, width)

# length = random.randint(1, 5)
# angle = random.randint(5, 25)
iterations = int(turtle.textinput("Recursive Trees", "Enter a iteration count less than 9:"))
length = int(turtle.textinput("Recursive Trees", "Enter a length less than 8:"))
angle = int(turtle.textinput("Recursive Trees", "Enter an angle less than 25:"))
fallRes = turtle.textinput("Recursive Trees", "Is it fall? Y or N")
if fallRes == "Y" or fallRes == "y" or fallRes ==  "Yes" or fallRes ==  "yes":
    fallBool = True
if fallRes == "N" or fallRes == "n" or fallRes =="No" or fallRes =="no":
    fallBool = False

def recursiveTree(limiter, xPos = 0, yPos = 0, heading = 0):
    turtle.tracer(0,0)
    leafColor = -1
    if limiter > 0:
        lengthMod1 = random.randint(5, 10)
        angleMod1 = random.randint(0, 10)
        lengthMod2 = random.randint(5, 10)
        angleMod2 = random.randint(0, 10)
        turt1 = turtle.Turtle()
        turt2 = turtle.Turtle()
        turt1.pensize(2*limiter)
        turt2.pensize(2*limiter)
        turt1.color("brown")
        turt2.color("brown")
        if limiter == 1:
            turt1.pensize(20*limiter)
            turt2.pensize(20*limiter)
            turt1.color("green")
            turt2.color("green")
            leafColor = random.randint(0, 2)
        if leafColor == 0 and fallBool == True:
            turt2.color("red")
        if leafColor == 1 and fallBool == True:
            turt2.color("orange")
        if leafColor == 2 and fallBool == True:
            turt2.color("yellow")
        turt1.penup()
        turt2.penup()
        turt1.goto(xPos,yPos)
        turt1.left(heading)
        turt2.goto(xPos,yPos)
        turt2.left(heading)
        turt1.pendown()
        turt2.pendown()
        turt1.right(angle + angleMod1)
        turt1.forward((length + lengthMod1) * limiter)
        turt2.right((angle + angleMod2) * -1 )
        turt2.forward((length + lengthMod2)* limiter)
        turt1x = math.floor(turt1.xcor())
        turt1y = math.floor(turt1.ycor())
        turt1h = turt1.heading()
        turt2x = math.floor(turt2.xcor())
        turt2y = math.floor(turt2.ycor())
        turt2h = turt2.heading()
        limiter = limiter - 1
        turt1.hideturtle()
        turt2.hideturtle()
        if limiter == 0:
            turtle.update()
        recursiveTree(limiter, turt1x, turt1y, turt1h)
        recursiveTree(limiter, turt2x, turt2y, turt2h)
pen = turtle.Turtle()
pen.penup()
pen.goto(-950,500)
pen.write("Length: " + str(length) + " Angle: " + str(angle) + " Iterations: " + str(iterations), font=("Calibri", 16, "bold"))
pen.hideturtle()
trunk = turtle.Turtle()
trunk.color("brown")
trunk.pensize(iterations*2.5)
trunk.penup()
trunk.goto(0,-500)
trunk.left(90)
trunk.pendown()
trunk.forward(length*iterations*5)
trunk.hideturtle()
recursiveTree(iterations, trunk.xcor(), trunk.ycor(), trunk.heading())
turtle.done()
