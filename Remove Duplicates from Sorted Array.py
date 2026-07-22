# Remove Duplicates from Sorted Array
nums=[0,0,1,1,2,3,3,4,4]
List=[]
for i in range(len(nums)):
    unique=nums[i]
    for j in range(i+1,len(nums)):
        
