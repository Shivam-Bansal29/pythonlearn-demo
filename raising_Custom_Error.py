# Program to demo raising custom error
a=(input("Enter a String "))
if(a=="quit"):
  print(" only Quit is working ")
else:
  try:
      v=int(a)

  except ValueError:
    print("\n Cannot be covertd into int" )
  else: # thus this else is with the try block
    if(v<5 or v>9):
      raise ValueError("\n Entered string is not quit and not between 5-9")
    
  
      
