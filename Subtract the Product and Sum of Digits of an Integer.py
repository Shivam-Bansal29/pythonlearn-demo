#  Subtract the Product and Sum of Digits of an Integer
n=int(input("Enter a number "))
Sum=0
Product=1
while(n>0):
    rem=n%10
    Sum=Sum+rem
    Product=Product*rem
    n=n//10
print("The Subtraction of Product and Sum of Digits of an Integer = ",Product-
      Sum)
