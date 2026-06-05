# Snake water gun
import random
print("0. snake")
print("1. water")
print("2. Gun")
print("4. quit")
result = [                                             # This is like :-
          ["Draw","Win","Loss"],     #player\computer-> |Snake | Water | Gun
          ["Loss","Draw","Win"],      #  Snake          |Draw  | Win   |loss
          ["Win","Loss","Draw"]       #  Water          |Loss  | Draw  |Win
          ]                           #  Gun            |Win   | Loss  |Draw  
dic={0:"Snake",1:"Water",2:"Gun"}
while True:
     choice = int(input("\n Enter your choice "))

     if(choice==4):
          print("You chosse to quit ")
          break
     elif(choice > 2 or choice < 0):
          print("wrong Input")
          continue
     else:
          computer = random.randint(0,2) # randint means random integer betweem 1-3
          print(" You entered ",dic[choice])
          print(" Computer chosed ",dic[computer])
          print(result[choice][computer])
     
