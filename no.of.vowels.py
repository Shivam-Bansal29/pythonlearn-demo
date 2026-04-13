a=input("Enter a string : ")
x=['a','e','i','o','u']
count=0
m=[]
for i in a.lower():
    if i in x:
        count+=1
        m.append(i) 
print("there are ",count," Vowels in ",a)
print(" And vowels in ",a," are ",m)
