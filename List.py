# Take a list from user and find its sum
n=int(input("Enter a number "))
a=[]
for i in range(0,n):
    n=int(input("enter number of list"))
    a.append(n) # this will append means add n at the end of list till loop srun
print(a)
total=0
for i in a: # here i is not behave like index it will take each value of list
    total=total+i # so we dont do a[i],just i as it have value of a[1],a[2],a[n]
print("total of members of list",total)
# LIST METHODS

'''a.sort()
print("after sortiing \n ",a)'''
'''a.reverse()
print("After reverse \n ",a)'''
'''a.insert(3,273) # it will insert 273 at 3 index
print("iinserting 273 at 3rd index \n "a)'''
m=[34,45,4353,'aa',"Shiva,"]
"""a.extend(m)
print("After extending m to a  \n ",a)"""
# demo tupple
'''
tup=(23,423,432,23,"Shibam ",234,34.243)
for xx in tup:
    print(xx)
''' 
