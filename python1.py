# Simple Snake Game Python 3 for Bigenners
# By Nusratov Eldor, for telegram @elyahk
# Part 1. Getting Started

import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game By @elyahk")
wn.bgcolor("green")
wn.setup(width=600, height=600)

# Snake head
head = turtle.Turtle()
head.shape('circle')
head.speed(0)
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"
wn.tracer(0)  # Turn of the screen updates

# Foods
food = turtle.Turtle()
food.shape('circle')
food.speed(0)
food.color("red")
food.penup()
food.goto(100, 40)

# Pen
pen = turtle.Turtle()
# pen.shape()
pen.color("red")
pen.penup()
pen.goto(0, 260)
pen.write("SCORE {} AND HIGH SCORE {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard Binding
turtle.listen()
turtle.onkeypress(go_up, 'w')
turtle.onkeypress(go_left, 'a')
turtle.onkeypress(go_right, "d")
turtle.onkey(go_down, "s")

segments = []
while True:
    wn.update()

    # Eat foods
    if head.distance(food) < 20:
        x1 = food.xcor()
        y1 = food.ycor()
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.shape('square')
        new_segment.speed(0)
        new_segment.color("grey")
        new_segment.penup()
        new_segment.goto(x1, y1)
        segments.append(new_segment)

        score += 10
        if high_score < score :
            high_score = score

        pen.clear()
        pen.write("SCORE {} AND HIGH SCORE {} ".format(score, high_score), align="center",font=("Courier", 24, "normal"))


    # Check the collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        head.direction = "stop"
        time.sleep(1)
        score = 0

    # Move the end segments first reserve in order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the first segment to head position
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Check the collision with body

    move()

    for segment in segments:
        if head.distance(segment) < 20:
            head.goto(0, 0)

            head.direction = "stop"
            time.sleep(1)
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0

    time.sleep(delay)

wn.mainloop()
