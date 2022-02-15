"""TODO: draw a beautiful mountain scene."""


__author__ = "730461954"


from turtle import Turtle, colormode, tracer, update, done


def main() -> None:
    """The entrypoint of my scene."""
    turt: Turtle = Turtle()
    colormode()
    tracer(0, 0)
    """The following mountain functions are my attempt at a mountain range."""
    draw_mount(turt, -250, 165, 200)
    draw_mount(turt, -300, 165, 200)
    draw_mount(turt, -200, 165, 200)
    draw_mount(turt, -320, 125, 200)
    draw_mount(turt, -160, 125, 200)
    draw_mount(turt, -420, 165, 225)
    draw_mount(turt, -380, 165, 215)
    """Other parts of my drawing."""
    draw_sun(turt, 300, 260, 30)
    draw_grass(turt, -800, 165, 2000)
    draw_water(turt, -800, -150, 2000)
    draw_house(turt, 100, 0, 100)
    update()
    done()


"""TODO: define the procedures for other components in your scene here"""


def reset_location(turt: Turtle, x: float, y: float) -> None:
    turt.up()
    turt.home()
    turt.goto(x, y)
    turt.down()


def draw_mount(turt: Turtle, x: float, y: float, side_length: float) -> None:
    """Draws a triangular mountain with some ice at the peak."""
    turt.ht()
    turt.speed(100)
    turt.up()
    turt.goto(x, y)
    turt.setheading(0)
    turt.down()
    turt.begin_fill()
    turt.fillcolor("gray")
    i: int = 0 
    while i < 4:
        turt.forward(side_length)
        turt.right(-120)
        i += 1
    turt.end_fill()
    turt.fillcolor("blue")
    turt.forward(side_length * .80)
    turt.left(60)
    """Adding some blue ice."""
    turt.begin_fill()
    while i < 7:
        turt.forward(side_length * .2)  
        turt.right(120)
        i += 1
    turt.end_fill()
    """Adding some white snow trails."""
    side_length = side_length * .2
    while i < 20:
        turt.color("white")
        side_length = side_length * .97
        turt.forward(side_length)
        turt.right(121.5)
        i += 1


def draw_sun(turt: Turtle, x: float, y: float, radius: float) -> None:
    """Draws some nice sunshine."""
    # turt.ht()
    turt.speed(100)
    reset_location(turt, x, y)
    turt.begin_fill()
    turt.fillcolor("orange")
    turt.circle(radius)
    turt.end_fill()


def draw_grass(turt: Turtle, x: float, y: float, side_length: float) -> None:
    """Draws some green grass."""
    turt.ht()
    turt.speed(1000)
    reset_location(turt, x, y)
    turt.fillcolor("green")
    turt.begin_fill()
    i: int = 0 
    while i < 4:
        turt.forward(side_length)
        turt.right(90)
        i += 1
    turt.end_fill()


def draw_water(turt: Turtle, x: float, y: float, side_length: float) -> None:
    """draws some deep blue water."""
    turt.ht()
    turt.speed(1000)
    turt.up()
    turt.home()
    turt.goto(x, y)
    turt.fillcolor("blue")
    turt.begin_fill()
    i: int = 0 
    while i < 4:
        turt.forward(side_length)
        turt.right(90)
        i += 1 
    turt.end_fill()


def draw_house(turt: Turtle, x: float, y: float, size: float) -> None:
    """Draws a brown house."""
    turt.ht()
    turt.speed(100)
    reset_location(turt, x, y)
    turt.fillcolor("brown")
    turt.begin_fill()
    i: int = 0 
    while i < 4:
        turt.forward(size)
        turt.right(90)
        i += 1
    turt.end_fill()
    reset_location(turt, x, y)
    turt.begin_fill()
    while i < 7:
        turt.forward(size)
        turt.left(120)
        i += 1
    turt.end_fill()
    turt.up()
    turt.forward(size * .4)
    turt.right(90)
    turt.forward(size)
    turt.left(90)
    turt.fillcolor("black")
    turt.begin_fill()
    turt.forward(size * .2)
    turt.left(90)
    turt.forward(size * .4)
    turt.left(90)
    turt.forward(size * .2)
    turt.end_fill()


if __name__ == "__main__":
    main()