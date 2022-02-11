import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main():
    turtle.setup(600,400)
    turtle.penup()
    turtle.goto(-100,70)
    turtle.pendown()
    turtle.pencolor("blue")
    turtle.pensize(2)
    size=300;level=3
    angle=120
    totalangle=0
    while totalangle<360:
        koch(size,level)        
        turtle.right(angle) 
        totalangle+=angle
    turtle.hideturtle()
    turtle.done()

main()