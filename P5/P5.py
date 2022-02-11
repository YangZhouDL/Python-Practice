import time
scale=50
start=time.perf_counter()
print("开始执行".center(scale//2,"-"))
for i in range(scale+1):
    a=i*"*"
    b="#"*(scale-i)
    c=int((i/scale)*100)    
    last=time.perf_counter()-start
    print("\r{}%[{}->{}]{:.2f}s".format(c,a,b,last),end=" ")
    time.sleep(0.1)
print("\n"+"结束执行".center(scale//2,"-"))