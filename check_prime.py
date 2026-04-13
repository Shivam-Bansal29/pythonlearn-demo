# program to find prime number by for else
x=int(input("\n Give all prime nmber till  "))
if(x<2):
    print("0 and 1 are neither prime nor composite ")
else:
    for i in range(2,x):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
    '''for i in range(2,x):
        f=0
        for j in range(2,i):
            if(i%j==0):
                f=f+1
                break
        if(f==0):
            print(i)'''
    
    
