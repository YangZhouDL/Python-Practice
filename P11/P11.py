import jieba
txt=open("threekingdoms.txt","r",encoding="utf-8").read()
excludes={"将军","却说","荆州","二人","不可","不能","如此","商议","如何","次日","主公","军士","左右","军马","大喜"}
words=jieba.lcut(txt)
count={}
for word in words:
    if len(word)==1:
        continue
    elif word=="诸葛亮" or word=="孔明曰":
        rword="孔明"
    elif word=="关公" or word=="云长":
        rword="关羽"
    elif word=="玄德" or word=="玄德曰":
        rword="刘备"
    elif word=="孟德" or word=="丞相":
        rword="曹操"
    else:
        rword=word
    count[rword]=count.get(rword,0)+1
for word in excludes:
    del count[word]
items=list(count.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,num=items[i]
    print("{}\t{}".format(word,num))
