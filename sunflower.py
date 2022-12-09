import turtle

skk = turtle.Turtle()
skk2 = turtle.Turtle()
turtle.colormode(255)
skk.speed(100)
skk2.speed(100)
skk.color("dark green")
skk2.color("tan")

angle = 137.5
penSize = 10
pedalStretcher = 1
pedalSpacer = 0
genSpacer = 15

for i in range(300):
    dynamicPenSize = penSize+i/7
    skk.pensize(dynamicPenSize)
    skk2.pensize(dynamicPenSize-3)
    if skk.pensize() > 40:
        pedalStretcher = 120
        pedalSpacer = 10
        skk.color("yellow")
        skk2.color("orange")
        skk2.pensize(3)
    skk.penup()
    skk.right(angle*i)
    skk.forward(genSpacer+i+pedalSpacer)
    skk.pendown()
    skk.forward(pedalStretcher)
    skk.penup()
    skk.backward(i+genSpacer+pedalStretcher+pedalSpacer)
    skk.left(angle*i)
    skk2.penup()
    skk2.right(angle*i)
    skk2.forward(genSpacer+i+pedalSpacer)
    skk2.pendown()
    skk2.forward(pedalStretcher)
    skk2.penup()
    skk2.backward(i+genSpacer+pedalStretcher+pedalSpacer)
    skk2.left(angle*i)
turtle.done()
