import random
import turtle


t = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)

t.shape()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = r, g, b
    return random_color
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
#           "wheat", "SlateGray", "SeaGreen"]


heading = [0, 90, 180, 270]
t.speed("fastest")
t.pensize(30)
# rand_heading = random.choice(heading)
# direction = rand_heading

for _ in range(200):

    t.color(random_color())
    t.forward(50)
    t.setheading(random.choice(heading))
