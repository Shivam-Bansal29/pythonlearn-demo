# Program to check wheteher the number is prime or not
while True:
    n=int(input("Enter the number "))
    f1=0
    if(n<2):
        print("0 and 1 are neither Prime nor Composite ")
    else:
        for i in range(2,n//2):
            if(n%i==0):
                f1+=1
                break
    
        if(f1<1):
            print("\n The numebr is prime ")
        else:
            print("\n The number is composite ")
    
    
