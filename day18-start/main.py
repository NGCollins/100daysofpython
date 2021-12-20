from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# def change_color():
#     R = random.randrange(0, 256, 10)
#     G = random.randrange(0, 256, 10)
#     B = random.randrange(0, 256, 10)
#
#     Turtle.color(R, G, B)


number_of_sides = 3


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#     for shape_side in range(3, 11):
#         draw_shape(shape_side)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(-90)
timmy_the_turtle.forward(100)

screen = Screen()
screen.exitonclick()
