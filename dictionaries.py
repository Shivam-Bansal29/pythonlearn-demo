# Dictionaries
d={"Name":" Shivam Bansal ",
   "Class":" BCA ",
   2151:" ME "}
s={111:"Mani",999:"Harry"}
d.update(s)
print(d)
'''s.clear()
print(s) this function will clear the dictinory and  gave nul {}'''
print(d["Name"])
print(d.keys())
print(d.values())
print(d.items())
for i in d.keys():
    print(i,d[i])
for i in d.get("Class"):
    print(i)
for i,k in  d.items(): # it will gave key value pair and in i key is stored
    # and in k values will be stored
    print(i,k)


