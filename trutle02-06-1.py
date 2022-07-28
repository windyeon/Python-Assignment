import turtle

myT = None
myT2 = None

myT = turtle.Turtle()
myT.shape('turtle')

myT2 = turtle.Turtle()
myT2.color("white")


for i in range(0,4) :
    myT.forward(200)
    myT.right(90)
    myT2.forward(200)
    myT2.right(90)

turtle.done()
