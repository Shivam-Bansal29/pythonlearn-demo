# Shuffle the Array
List=[6,82,289,329,983,38,833,3982]
mid=4
array=[]
print(List)
for i in range(0,mid):
    array.append(List[i])
    array.append(List[mid+i])
print(array)
        
