import turtle

colors = ["red","orange","yellow","green","blue","indigo","violet"]

turtle.speed(500)
turtle.bgcolor("white") 
turtle.pensize(1) 

for i in range(2):
    turtle.color(colors[i % len(colors)])
    turtle.forward(10)
    turtle.left(9) 
    turtle.forward(30)

turtle.done()