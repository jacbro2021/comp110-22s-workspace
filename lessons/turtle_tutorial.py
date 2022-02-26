"""A short tutorial on Turle."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

side_length: float = 300

leo.speed(10)
leo.ht()

colormode()
leo.color("red", "blue")

leo.begin_fill()

leo.up()
leo.goto(-150, 100)
leo.down()

i: int = 0 
while i < 3:
    leo.forward(side_length)
    leo.right(120)
    i += 1

leo.end_fill()

bob: Turtle = Turtle()

bob.color("black")
bob.up()
bob.goto(-150, 100)
bob.down()
bob.speed(1000)
bob.ht()

i: int = 0 
while i < 100:
    side_length = side_length * .95
    bob.forward(side_length)
    bob.right(121.5)
    i += 1

done()
