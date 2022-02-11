def getText():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()
    for ch in '~`!@#$%^&*()_+-={}:"<>?,./;[]\|':
        txt=txt.replace(ch," ")
    return txt

hamlet=getText()
words=hamlet.split()
count={}
for word in words:
    count[word]=count.get(word,0)+1
items=list(count.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,num=items[i]
    print("{}\t{}".format(word,num))