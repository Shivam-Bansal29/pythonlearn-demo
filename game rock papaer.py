import random
w=0
l=0
t=0
print(" ' Enter any number greater than 4 to get results ' " )
print(' Press 1 for Paper 📄 ')
print(' Press 2 for Rock 🪨 ')
print(' Press 3 for Scissor  ✂ ')
while True :
    x = int(input("\n press 1,2,3 :-"))
    if x >=4 :
        break
    
    words = [1,2,3]
    d={1:"Paper 📄 ",2:"Rock 🪨",3:" Scissor ✂ "}
    y= random.choice(words) 
    print("computer chosse = ",d[y])
    print(" your choice = ", d[x])
    if x==y:
        print(" match is tie 🤝 ")
        t+=1
    elif x==2:#rock
        if y==1:#paper
            l+=1
            print(" ohh ! you loose 😢")
        else :
            print(" Hurrah ! You Won 😄 ")
            w+=1 
            
    elif x==3:# scisoor
        if y==2:#rock
            print(" ohh ! you loose 😢  ")
            l+=1
        else:
            print(" hurray ! you win 😄 ")
            w+=1
    elif x==1:# paper
        if y==2:#rock
            print(" hurrah ! you win 😄 ")
            w+=1
        else :
             print(" ohh ! you loose 😢")
             l+=1
    else :
        print(" invalid number ")
   
print(" Total Matches = " ,w+l+t)
print(" you won 😄 = ",w)
print(" you loose 😢 = ",l)
print(" tie 🤝 = ",t)
if(t>l):
    print("\n You won and compuetr losses ")
else:
    print("\n You losse and compuetr won ")




    
