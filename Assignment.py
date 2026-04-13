# Assignmnet 1
u=int(input("Enter a range "))
def multiple(i):
    if(i%3==0 and i%5==0):
        print("FIZZBUZZ")        
    elif(i%3==0):
        print("FIzz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)

for i in range(1,u):
    multiple(i)
