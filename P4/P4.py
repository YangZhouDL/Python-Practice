def dayup(df):
    daybase=1
    #dayfactor=0.01
    for i in range(365):
        r=i+1
        if r%7 in [6,0]:
            daybase=daybase*(1-0.01)
        else:
            daybase=daybase*(1+df)
    #print("最终：{:.2f}".format(daybase))
    return daybase
dayfactor=0.01
while dayup(dayfactor)<37.78:
    dayfactor+=0.001
print("甲工作日需每天进步：{:.3f}%".format(dayfactor*100))
