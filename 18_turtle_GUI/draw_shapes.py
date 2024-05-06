import random
import turtle


t = turtle.Turtle()
screen = turtle.Screen()

t.shape()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
          "SlateGray", "SeaGreen"]

# num_sides = int(screen.textinput(title="Draw a Shape", prompt="How many sides?"))
# play_again = False

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for shape_side_n in range(3, 11):
    t.color(random.choice(colors))
    draw_shape(shape_side_n)

    # shape = screen.textinput(title="", prompt="What shape (pentagon/square)?")


#     if shape == "pentagon":
#         for _ in range(5):
#             t.forward(100)
#             t.right(72)
#
#     if shape == "square":
#         for _ in range(4):
#             t.forward(100)
#             t.right(90)
#
#
# while play_again:
#     play_shape()
#     again = screen.textinput(title="", prompt="Would you like to go again (y/n)?")
#     play_again = again.lower() in ("y" or "yes")

screen.exitonclick()
