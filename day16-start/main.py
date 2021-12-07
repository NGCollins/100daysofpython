from turtle import Turtle, Screen
# import another_module
# print(another_module.another_variable)

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon",["Pikachu","Squirtle","Mew","Charmandar"])
table.add_column("Type",["Electric","Water","Normal","Fire"])
table.align = "l"
print(table)

