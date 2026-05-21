nums=[2,23,1,12,32]
print(nums)
test=[] # Emmpty list
for i in range(0,len(nums)):
    if(i==0):
        test.append(nums[i])
    else:
        test.append(nums[i]+test[i-1])
print(test)
