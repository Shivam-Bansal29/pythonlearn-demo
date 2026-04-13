# Program to find sum of 
num=int(input("Enter a number : "))
Sum=0
while(num>0):
    rem=num%10
    Sum=Sum+rem
    num//=10
print("\n The sum of digit is ",Sum)

