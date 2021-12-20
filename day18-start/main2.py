from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

color = ["cyan", "deep pink", "firebrick", "green", "blue violet", "powder blue", "powder blue", "medium purple",
         "salmon"]
tim.speed(0)
tim.pensize(10)
screen.colormode(255)


def change_color():
    R = random.randrange(0, 256, 10)
    G = random.randrange(0, 256, 10)
    B = random.randrange(0, 256, 10)

    return tim.color(R, G, B)


def random_walk():
    change_color()
    tim.forward(30)
    tim.right(random.randrange(-360, 360, 90))


for _ in range(100):
    random_walk()

screen.exitonclick()
