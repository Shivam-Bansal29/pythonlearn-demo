# program to demo time module
import time 
name=input("\n Enter your name ")
print(time.strftime("%H:%M:%S"))
print(time.localtime())
time.sleep(3)
h=int(time.strftime("%H")) # as this function will return time as string to applly
# comaprisn operator on it, it has to be an integer so i convert string into int 
if(h==00):
    print("\n Good night ",name)
elif(5<=h<12):
    print("\n Good morning ",name)
elif(12<=h<17):
    print("\n Good Evening ",name)
else:
    print("\n Good night ",name)

