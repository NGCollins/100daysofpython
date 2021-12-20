# import colorgram
#
# # Extract 6 colors from an image.
# rgb_colors = []
# colors = colorgram.extract('hirst_spot_painting.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
from turtle import Turtle, Screen
import random
color_list=[(190, 176, 33), (236, 70, 31), (182, 45, 67), (216, 227, 220),
 (156, 31, 44), (68, 35, 56), (237, 222, 227), (121, 164, 196)]

turtle = Turtle()
screen = Screen()
random_color = random.choice(color_list)
screen.colormode(255)
turtle.setheading(225)
turtle.penup()
turtle.forward(500)
turtle.setheading(0)
turtle.speed("fastest")
turtle.hideturtle()
def generate_random_hirst():
    screen.screensize(300, 300)
    number_of_dots = 100
    for dot_count in range(1,number_of_dots+1):
        turtle.dot(20,random.choice(color_list))
        turtle.fd(50)
        if dot_count %10 == 0:
            turtle.setheading(90)
            turtle.forward(50)
            turtle.setheading(180)
            turtle.forward(500)
            turtle.setheading(0)


generate_random_hirst()
print(screen.window_width())
print(screen.window_height())
screen.exitonclick()


