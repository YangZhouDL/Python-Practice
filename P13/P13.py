import random
def getInfo():
    sa=eval(input("请输入A的能力值："))
    sb=eval(input("请输入B的能力值："))
    n=eval(input("请输入比赛场数："))
    return n,sa,sb

def oneBi(Sa,Sb,Flag):
    jud=random.randint(1,100)
    sa=Sa;sb=Sb
    if Flag==1:
        if sa>=jud:
            Flag=1
        else:
            Flag=0
    else:
        if sb>=jud:
            Flag=0
        else:
            Flag=1
    return Flag

def allBi(n,sa,sb):
    ca=0;cb=0;flag=1
    for i in range(n):
        flag=oneBi(sa,sb,flag)
        if flag==1:
            ca=ca+1
            print("第{}场A胜利".format(i+1))
        else:
            cb=cb+1
            print("第{}场B胜利".format(i+1))
    return ca,cb

def main():
    n,sa,sb=getInfo()
    ca,cb=allBi(n,sa,sb)
    print("A胜场数为{}\tB胜场数为{}".format(ca,cb))
    print("A的胜率为{:.2f}%\tB的胜率为{:.2f}%".format((ca/n)*100,(cb/n)*100))
    return 0

main()

