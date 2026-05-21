# Richest Customer Wealth
account=[[100,5778,10],[7576,8749,94],[685,3487,43299],[47437,3782,3]]
Money=[]
for i in account:
    wealth=0
    for j in i:
        wealth=wealth+j
    Money.append(wealth)
Max=Money[0]
for x in range(0,len(Money)):
    if(Money[x]>Max):
        Max=Money[x]
        cos=x+1
print(f"{cos} person has has max wealth {Max}")
    
               
                 
