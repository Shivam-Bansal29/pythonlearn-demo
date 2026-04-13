# program to find factorial of a number by using recurssion function
a=int(input("Enter a number "))
def recursion(x):
    if(x==0):
        return 1
    else:
        return(x*recursion(x-1))
        
fac=recursion(a)
print(f"The Factorial of {a} is {fac}")
# Fibonnaci series by looping

A=0
b=1
for i in range(a+1):
    print(A,end=" ")
    c=A+b
    A=b
    b=c
print("\n\n")
# Fibonnaci by recursion
def fib(r):
    if(r==0):
        return 0
    elif(r==1):
        return 1
    else:
        return fib(r-1)+fib(r-2)
        
        
fibb=fib(a)
print(fibb)
  
