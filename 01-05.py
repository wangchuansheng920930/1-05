from turtle import 
import random
import time

def change_color(t)
    R = random.random()
    B = random.random()
    G = random.random()
    t.pencolor(R, G, B)

def display_msg(msg)
    for c in msg
        change_color(t)
        t.write(c, move=False, align=left, font=(Arial, 36, normal))
        t.forward(50)
    
width = 800
height = 200
xPos = -(width2)
yPos = 0
setup(width, height)

t = Turtle(turtle)
t.speed(0)
t.hideturtle()
t.begin_fill()
#t._delay(25)
t.penup()

while True
    t.goto(xPos + 10, yPos)
    display_msg(最愛寶貝❤️)
    t.goto(xPos + 10, yPos - 60)
    display_msg(20200105 傳說製)
    time.sleep(2)
    t.clear()

t.end_fill()
done()
