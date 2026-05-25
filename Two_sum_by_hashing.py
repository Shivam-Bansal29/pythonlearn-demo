#Two sum by hashing
nums=[4,4,6,5,3,1,4,3,13,9]
target = 12
dic={}
for i in range(len(nums)):
    rem = target-nums[i]
    if rem in dic:
        print(dic[rem],i)
    dic[nums[i]]=i
    print(dic)
