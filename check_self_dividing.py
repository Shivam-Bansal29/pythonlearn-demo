# Self dividing numbers in a particular range, self dividing are those 
# which are divisible by All the digits in number like 128 is divisble by 1,2,8
left=int(input("\n Enter a number "))
right=int(input("\n Enter a number "))
k=[]
for i in range(left,right+1):
    rem=0
    n=i
    while(n>0):
        rem=n%10
        n=n//10
        if(rem==0):
            break
        elif(i%rem!=0):
            break
    else:
        k.append(i)
print(k)
        
   
        
