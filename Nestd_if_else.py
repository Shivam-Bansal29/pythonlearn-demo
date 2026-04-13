# Nested if else
# this statement is used to take ,ultiple inputs at same time'
""".split() will divede the inputs on the basis os pace if 213 23 324 so split wil
divide 213 into one 23 into second if split not used whole input is taken as one
input"213 23 324" """
# map will asign value to a,b,c variabels separated by split 
a,b,c=map(int,input("Enter Three  number ").split())
if(a>b):
          if(a>c):
             print(a,"is greater ")
          else:
              print(c,"is greater ")
else:
    if(b>c):
        print(b,"is graeter ")
    else:
        print(c,"is greater")
    
