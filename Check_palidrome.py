# program to check whether a number is palidrome or not
a=int(input("Enter a number "))
n=a
number=0
while(n>0):
    rem=n%10
    number=(number*10)+rem
    n=n//10
print("\nThe reversed number is ",number)
if(number==a):
    print("\n Number is palidrome ")
else:
    print("\n Number is not Palidrome ")
    
    
