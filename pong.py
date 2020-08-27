import turtle
import random

tur = turtle.Screen()

tur.title("Pong")
tur.bgcolor("black")
tur.setup(width=800, height=600)
tur.tracer(0)

# player1
jug1 = turtle.Turtle()
jug1.speed(0)
jug1.shape("square")
jug1.color("white")
jug1.shapesize(stretch_wid=5, stretch_len=1)
jug1.penup()
jug1.goto(-350, 0)

# player2
jug2 = turtle.Turtle()
jug2.speed(0)
jug2.shape("square")
jug2.color("white")
jug2.shapesize(stretch_wid=5, stretch_len=1)
jug2.penup()
jug2.goto(350, 0)

# ball
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = random.randint(-2, 2)
bola.dy = random.randint(-2, 2)
while bola.dx == 0 or bola.dy == 0:
	bola.dx = random.randint(2, 0)
	bola.dy = random.randint(-2, 2)

# score
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 255)
puntaje1 = 0
puntaje2 = 0
marcador.write("Player 1: {}       Player 2: {}".format(puntaje1, puntaje2), align="center", font=("Courier", 24, "normal"))

jugando = False

# Functions
def jug1_up():
    y = jug1.ycor()
    y += 20
    jug1.sety(y)

def jug1_down():
    y = jug1.ycor()
    y -= 20
    jug1.sety(y)

def jug2_up():
    y = jug2.ycor()
    y += 20
    jug2.sety(y) 

def jug2_down():
    y = jug2.ycor()
    y -= 20
    jug2.sety(y)

# Keyboard binding
tur.listen()
tur.onkey(jug1_up, "w")
tur.onkey(jug1_down, "s")
tur.onkey(jug2_up, "Up")
tur.onkey(jug2_down, "Down")

a = 0

while True:
    tur.update()

    # ball movement
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # limits (boundaries)
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
    elif bola.ycor() < -280:
        bola.sety(-280)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0,0)
        a += 1
        if a == 5:
            puntaje1 += 1
        marcador.clear()
        marcador.write("Player 1: {}       Player 2: {}".format(puntaje1, puntaje2), align="center", font=("Courier", 24, "normal"))
        bola.dx = 2
    elif bola.xcor() < -390:
        bola.goto(0, 0)
        a += 1
        if a == 5:
            puntaje2 += 1
        marcador.clear()
        marcador.write("Player 1: {}       Player 2: {}".format(puntaje1, puntaje2), align="center", font=("Courier", 24, "normal"))
        bola.dx = -2

    # collision
    if bola.xcor() > 330 and bola.xcor() < 340 and bola.ycor() < jug2.ycor() + 50 and bola.ycor() > jug2.ycor() - 50:
        bola.setx(330)
        bola.dx *= -1.2
    elif bola.xcor() < -330 and bola.xcor() > -340 and bola.ycor() < jug1.ycor() + 50 and bola.ycor() > jug1.ycor() - 50:
        bola.setx(-330)
        bola.dx *= -1.2  







