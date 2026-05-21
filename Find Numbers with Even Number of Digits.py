# Find Numbers with Even Number of Digits
nums=[62,823,392,27138,21,23,32,432,823,329,9239,3782,932823,76111]
even=0
print(nums)
for i in nums:
    digit=len(str(i))  
    if(digit%2==0):
        even+=1
print(even)
        
