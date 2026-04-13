# Program to revesre the number
while True:
    num=int(input("Enter a number "))
    Sum=0
    rev=0
    while(num>0):
        rev=num%10
        Sum=Sum*10+rev
        num=num//10 # // will give onlu integer number as in pyhton a variable can be flaot integr
    print("The reverse of number is ",Sum)
