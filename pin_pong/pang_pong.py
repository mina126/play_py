import turtle

wind = turtle.Screen()
wind.title("ping pong")
wind.bgcolor("Black")
wind.setup(width=800, height=600)
wind.tracer(0)

# madrb_1

madrb1 = turtle.Turtle()
madrb1.speed(0)
madrb1.shape("square")
madrb1.shapesize(stretch_len=1, stretch_wid=6)
madrb1.color("blue")
madrb1.penup()
madrb1.goto(-350, 0)
# madrb_2
madrb2 = turtle.Turtle()
madrb2.speed(0)
madrb2.shape("square")
madrb2.shapesize(stretch_len=1, stretch_wid=6)
madrb2.color("red")
madrb2.penup()
madrb2.goto(350, 0)
# boll
boll = turtle.Turtle()
boll.speed(0)
boll.shape("circle")
boll.color("white")
boll.penup()
boll.goto(0, 0)
boll.dx = 0.3
boll.dy = 0.3

# score
player1 = 0
player2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(
    f"player1 = {player1} player2 = {player2}",
    align="center",
    font=("Courier", 20, "normal"),
)


# t7rek al madrb
def madrb1_up():
    y = madrb1.ycor()
    y += 25
    madrb1.sety(y)


def madrb1_down():
    y = madrb1.ycor()
    y -= 25
    madrb1.sety(y)


# al madb al tane
def madrb2_up():
    y = madrb2.ycor()
    y += 25
    madrb2.sety(y)


def madrb2_down():
    y = madrb2.ycor()
    y -= 25
    madrb2.sety(y)


# t7rek al mdard
wind.listen()
wind.onkeypress(madrb1_up, "w")
wind.onkeypress(madrb1_down, "s")
wind.onkeypress(madrb2_up, "Up")
wind.onkeypress(madrb2_down, "Down")
while True:
    wind.update()
    # move the ball
    boll.setx(boll.xcor() + boll.dx)
    boll.sety(boll.ycor() + boll.dy)
    # lw al cora at7rken mn mcanha t5bt w targ3
    if boll.ycor() > 290:
        boll.seth(290)
        boll.dy *= -1
    if boll.ycor() < -290:
        boll.seth(-290)
        boll.dy *= -1

    if boll.xcor() > 390:
        boll.goto(0, 0)
        boll.dx *= -1
        player1 += 1
        score.clear()
        score.write(
            f"player1 = {player1} player2 = {player2}",
            align="center",
            font=("Courier", 20, "normal"),
        )

    if boll.xcor() < -390:
        boll.goto(0, 0)
        boll.dx *= -1
        player2 += 1
        score.clear()
        score.write(
            f"player1 = {player1} player2 = {player2}",
            align="center",
            font=("Courier", 20, "normal"),
        )

    if (boll.xcor() > 340 and boll.xcor() < 350) and (
        boll.ycor() < madrb2.ycor() + 40 and boll.ycor() > madrb2.ycor() - 40
    ):
        boll.setx(340)
        boll.dx *= -1

    if (boll.xcor() < -340 and boll.xcor() > -350) and (
        boll.ycor() < madrb1.ycor() + 40 and boll.ycor() > madrb1.ycor() - 40
    ):
        boll.setx(-340)
        boll.dx *= -1
