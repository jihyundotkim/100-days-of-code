from turtle import Turtle, Screen

thomas = Turtle()
screen = Screen()
screen.listen()


def w():
    thomas.forward(10)


def s():
    thomas.backward(10)


def a():
    thomas.left(5)


def d():
    thomas.right(5)


def c():
    thomas.clear()
    thomas.penup()
    thomas.home()
    thomas.pendown()


screen.onkey(w, "w")
screen.onkey(a, "a")
screen.onkey(s, "s")
screen.onkey(d, "d")
screen.onkey(c, "c")
screen.exitonclick()
