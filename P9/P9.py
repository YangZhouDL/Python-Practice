def getNum():
    numbers=[]
    inum=(input("请输入一个数（0退出）："))
    while inum!='0':
        numbers.append(eval(inum))
        inum=(input("请输入一个数（0退出）："))
    return numbers

def average(numbers):
    s=0.0
    for num in numbers:
        s+=num
    return s/len(numbers)

def dev(numbers,average):
    sdev=0.0
    for num in numbers:
        sdev=sdev+(num-average)**2
    return pow(sdev/(len(numbers)-1),0.5)

def mid(numbers):
    sorted(numbers)
    size=len(numbers)
    if size%2==0:
        mid=(numbers[size//2-1]+numbers[size//2])/2
    else:
        mid=numbers[size//2]
    return mid

n=getNum()
ave=average(n)
dev=dev(n,ave)
mid=mid(n)
print("\n平均数为：{:.3f}\n方差为：{:.3f}\n中位数为：{:.3f}".format(ave,dev,mid))