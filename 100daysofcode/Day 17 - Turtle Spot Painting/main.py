import turtle
import random


timmy = turtle.Turtle()
timmy.shape("turtle")
screen = turtle.Screen()
screen.colormode(255)
# for i in range(3, 11):
#     for j in range(i):
#         timmy.forward(100)
#         timmy.right(360/i)
#     timmy.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
timmy.speed("fastest")

# for i in range(200):
#     timmy.forward(15)
#     timmy.seth(random.choice([0,90,180,270]))
#     timmy.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

# for i in range(72):
#     timmy.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     timmy.circle(100)
#     timmy.left(5)

colors = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (155, 73, 60), (122, 167, 195), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183)]
timmy.penup()
for i in range(10):
    timmy.setpos(-200, i*50-200)
    for j in range(10):
        timmy.pendown()
        timmy.color(random.choice(colors))
        timmy.begin_fill()
        timmy.circle(10)
        timmy.end_fill()
        timmy.penup()
        if j < 10:
            timmy.forward(50)

screen.exitonclick()
