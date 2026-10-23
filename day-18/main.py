# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
color_list = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 74, 35), (7, 148, 95), (222, 170, 44), (182, 158, 47), (44, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 77), (85, 27, 91), (179, 40, 98), (243, 218, 57), (43, 170, 114), (210, 132, 166), (208, 56, 33), (239, 162, 194), (243, 166, 155), (150, 26, 25), (163, 211, 178), (25, 186, 226), (7, 115, 54), (137, 210, 233), (167, 193, 223), (74, 134, 185), (113, 6, 6)]

tim.setheading(225)
tim.penup()
tim.forward(350)
tim.setheading(0)

should_continue = True
number_of_dots = 100
while should_continue:
    for dot_count in range(10):
        number_of_dots -=1
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

    tim.setheading(90)
    tim.penup()
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.pendown()
    tim.setheading(0)

    if number_of_dots == 0:
        should_continue = False

screen = turtle_module.Screen()
screen.exitonclick()