# MAP 
def cube(x):
    return x*x*x
l=[1,2,3,4,5]
print(l)
newl =[]
# map are used at pace of using loop
for items in l:
    newl.append(cube(items))
print(newl)
new=map(cube ,l)
print(list(new))

# Filter
def filter_function(a):
    if(a>4):
        return True
# Filter Function will filter out the list items that qualify like here
# only >4 elements willl be gone to newl bcz they return true all <4 will return
# False so they don;t gos into newl
newl=filter(filter_function,l)
print(list(newl))

# reduce
def mysum(x,y):
    retunn x+y
    
    
 
def 
