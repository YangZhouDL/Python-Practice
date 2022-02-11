import time as t
import random as r
n=1000*1000
dot=0.0
start=t.perf_counter()
for i in range(n+1):
    x,y=r.random(),r.random()
    if pow(x**2+y**2,0.5)<1:
        dot=dot+1
pi=4*(dot/n)
last=t.perf_counter()-start
print("Pi={}".format(pi))
print("耗时：{:.5}s".format(last))
