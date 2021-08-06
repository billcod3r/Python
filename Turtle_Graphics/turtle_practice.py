import turtle              # 1.  import the modules
import random


wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

# your code goes here
# lance.forward(random.randrange(1, 10))


for distance in range(200):
    lance.forward(random.randrange(30, 100))
    andy.forward(random.randrange(30, 100))     
    
wn.exitonclick()
