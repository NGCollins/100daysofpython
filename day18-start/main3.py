from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()
screen.colormode(255)

tim.speed("fastest")

def change_color():
    R = random.randrange(0, 256, 10)
    G = random.randrange(0, 256, 10)
    B = random.randrange(0, 256, 10)

    return tim.color(R, G, B)


def draw_sprirograph(size_of_gap):
    for _ in range(int(360 /size_of_gap)):
        change_color()
        tim.circle(100)
        tim.seth(tim.heading() +size_of_gap)
        print(tim.heading())
draw_sprirograph(10)

screen.exitonclick()
