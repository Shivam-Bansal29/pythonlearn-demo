# 217. Contains Duplicate
nums=[1,2,3,4]
dic={}
for value in nums:
    if value in dic:
        dic[value]+=1
    else:
        dic[value]=1
    if(dic[value]>1):
        print("\n the list contains duplicate ")
        break
else:
    print("\n the list does not contain duplicate ")
    
