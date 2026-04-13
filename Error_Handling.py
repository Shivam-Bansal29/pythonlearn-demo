# Error handling by Using tru except
try:
    a=int(input("Enter a number "))
    s=[2,32,324,3]
    print(s[a])
except ValueError:
    print("\n Invalid input")
except IndexError:
    print(" the list has only members till 3 index")
print("\n This will run Even when error occurs")
try:
    print(3278/a)
except ZeroDivisionError:
    print("\n DIvision by 0 is not possible")

