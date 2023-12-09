import turtle

colors = ["red","orange","yellow","green","blue","indigo","violet"]

turtle.speed(2) # Set the drawing speed
turtle.bgcolor("white") # Set the background color
turtle.pensize(4) # Set the pen size

for i in range(36):
    turtle.color(colors[i % len(colors)]) # Cycle through the colors
    turtle.forward(200) # Increase the distance to make a bigger star
    turtle.left(170) # Turns the turtle left 170 degrees

turtle.done() # Finish the drawing

