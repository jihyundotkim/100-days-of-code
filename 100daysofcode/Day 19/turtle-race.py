from turtle import Turtle, Screen
import random

turtles = [Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle()]
turtles[0].color("red")
turtles[1].color("orange")
turtles[2].color("yellow")
turtles[3].color("green")
turtles[4].color("blue")
turtles[5].color("violet")

screen = Screen()

for i in range(6):
    turtles[i].shape("turtle")
    turtles[i].penup()
    turtles[i].setposition(-200, (30*i)-200)
    turtles[i].speed(1)

bet = screen.textinput("Make your bet!", "Which turtle will win?")

won = False
winner = ""
while not won:
    for j in range(6):
        turtles[j].forward(random.randint(10, 30))
        if turtles[j].xcor() >= 200:
            won = True
            winner = turtles[j].color()
            print(winner)
            break

if winner[0] == bet:
    print(f"You've won! The {winner[0]} turtle won the race!")
else:
    print(f"The {winner[0]} turtle won the race. You didn't win.")
    
screen.exitonclick()
