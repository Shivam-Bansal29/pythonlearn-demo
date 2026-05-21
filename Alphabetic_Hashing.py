# Program to demo alaphabetic Hashing,
Msg="Shivam IS My name"
find=[" ","S","I","a"]
dic={}
for m in Msg:
    if m in dic:
        dic[m]+=1
    else:
        dic[m]=1
for s in find:
    if s in dic:
        print(f"{s} exisit {dic[s]} times in lsit ")
    else:
        print(f"{s} does not exsist in the Message ")
