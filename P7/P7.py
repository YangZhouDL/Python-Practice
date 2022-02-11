import turtle as t
import time
def drawGap():
    t.penup()
    t.fd(5)

def drawline(draw):
    #drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.right(90)
    #drawGap()

def drawDigit(digit):
    t.color("black")
    drawline(True) if digit in [2,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    t.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    t.left(180)
    t.penup()
    t.fd(20)

def drawDate(date):
    #t.pencolor("black")          
    for i in date:
        if i=='+':
            t.pencolor("green")
            t.write('年',font=("Arial",24,"normal"))            
            t.fd(40)
        elif i=='-':
            t.pencolor("blue")
            t.write('月',font=("Arial",24,"normal"))            
            t.fd(40)
        elif i=='=':
            t.pencolor("purple")
            t.write('日',font=("Arial",24,"normal"))            
        else:
            drawDigit(eval(i))

def main():
    t.setup(800,300)
    t.penup()
    t.bk(285)
    t.pensize(5)
    date=time.strftime('%Y+%m-%d=',time.gmtime())
    drawDate(date)
    t.hideturtle()
    t.done()

main()