# Given an integer num, return the number of steps to reduce it to zero.
num=int(input("Enter a number "))
count=0
while (num>0):
    print(num)
    
    if(num%2==0):
        count+=1
        num=num//2
    else:
        count+=1
        num=num-1
        
print(count)

