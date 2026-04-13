# sum of number by recusion
n=int(input("Enter a number "))
def sum_of(g):
    if(g==1):
        return 1
    else:
        return g+sum_of(g-1)
suM=sum_of(n)
print("\n Sum of first ",n," number is ",suM)
def num(x):
    if(x==1):
        print(1)
        return 0
    else:
        num(x-1)
        print(x)
        
num(n)


