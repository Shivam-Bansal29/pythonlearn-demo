# Program to find wether a number is Armstrong or not
num=int(input(" Enter a number "))
n=num
def count(x):
    no_digit=0
    while(x>0):
        no_digit+=1
        x=x//10
    return no_digit
a=count(n)
arm=0

while(n>0):
    REM=n%10
    arm=REM**a+arm
    n=n//10
if(arm==num):
    print("\n The number is armstrong ")
else:
    print("\n the number is not armstrong ")
    
    

