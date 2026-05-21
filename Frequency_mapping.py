# Program to Frequency mapping
List=[4,3,2,4,2,2,1,2,3,1,2,4,5,32]
dic={} #Empty dictionary
for i in range(0,len(List)):
    if List[i] in dic:
        dic[List[i]]+=1

    else:
        dic[List[i]]=1
print(dic)

               
            
            
