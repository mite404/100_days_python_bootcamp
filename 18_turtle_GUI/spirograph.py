import random
import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)

t.shape()
t.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = r, g, b
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


draw_spirograph(5)

screen.exitonclick()
