import turtle               # allows us to use the turtles library
wn = turtle.w()        # creates a graphics window
wn.setup(540, 508)           # set window dimension

alex = turtle.Turtle()      # create a turtle named alex
alex.shape("turtle")        # alex looks like a turtle
alex.color('red')           # alex has a color


alex.circle(50)              # draws a circle of radius 50
alex.backward(50)            # alex moves 50 positions backward
alex.forward(50)             # alex moves 50 positions forward
alex.right(60)               # alex turns 60 degrees right
alex.left(60)
