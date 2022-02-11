r=25
area=3.1415*r*r
print(area)
print("{:.2f}".format(area))

import turtle
turtle.pensize(2)
turtle.circle(5)
turtle.circle(10)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)

from turtle import *
color('red','green')
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()
done()