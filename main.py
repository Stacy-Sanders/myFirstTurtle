"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
# from turtle import *
# color('blue', 'green')
# begin_fill()
# while  True :
#   forward(200)
#   left(170)
#   if abs(pos()) < 1 :
#     break
# end_fill()
# done()

tator = turtle.Turtle()
tator.shape('turtle')

# for c in ['red', 'green', 'yellow', 'blue']:
#     tator.color(c)
#     tator.forward(75)
#     tator.left(90)

for i in range(1,5) :
  tator.color('purple')
  tator.forward(70)
  tator.left(90)

tator.up()
tator.goto(-100, 0)
tator.down()
tator.color('blue')
tator.circle(50)

tator.up()
tator.goto(100, 100)
tator.down()
tator.color('red')
tator.stamp()

tator.up()
tator.goto(-75, -50)
tator.down()
