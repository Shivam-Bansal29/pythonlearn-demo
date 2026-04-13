ans=0               
money=0
wrong=0
''' hlo '''
def choice():
    """ KBC ME APKA SWAGAT HAI,THIS IS A DOCTSRING """
    ans=input("\n Tell me your answer ")
    wrong=money
    return ans.lower(),wrong
print(choice.__doc__)
print("Enter into the game of KBC ")
name=input("\n Enter your name : ")
print(f"So,{name} 1st question is for 1000 \n2nd question foor 2000\n3rd question for 5000\n4th question 10000\n5th question is for 20000\n6th question is for 50000\n7th is for 100000 \n8th and Last question is for 1000000")
questions=["Who is the current Prime minister of India ","What is value of pi",
           "Who developed C++ programming Language","Who developed Gnu Image Manipulation Program[GIMP]",
           "What is the Mascot of GIMP","Which river is the longest river of India ",
           "Who has Directetd the Famous Film Dhurandhar ","Who as Developed the Chat GPT"]
Answer1=["Narinder Modi","Rahul Gandhi ","Nirav Modi","Amit Shah"]
Answer2=["2.23","3.14","3.41","22.7"]
Answer3=["Dennis Ritchie","Jameson Gosling","John Mcarthy","Bjarne strostrup"]
Answer4=["Spencer kimbale & Pitter Mattis","Right Brothers","Adams and Tom","Nellambwr and Aramya"]
Answer5=["Wilber","Penguin","Cat","Colla"]
Answer6=["Ganga","Yammuna","Godawari","Brahmputra"]
Answer7=["Rohit Shetty","Aditya Dhar","Ranbeer Kapoor","Jay Shah"]
Answer8=["San Francisco","John Mc carthy","Tim cook","Modi"]
print(f"\n {name}, now we have discussed all the rules lets start the game \n")
while True:
    print(questions[0])
    print("\n",Answer1)
    ans,wrong=choice()
    if(ans==Answer1[0].lower()):
        print(f" The answer is corect you won 1000 ")
        money=1000
    else:
        print("\nYour answer is wrong ok You won Total Rs",wrong)
        break;
    
    print(questions[1])
    print("\n",Answer2)
    ans,wrong=choice()
    if(ans==Answer2[1].lower()):
        print(f" The answer is corect you won 2000 ")
        money+=1000
    else:
        print("\nYour answer is wrong ok You won Total Rs",wrong)
        break;
    
    print(questions[2])
    print("\n",Answer3)
    ans,wrong=choice()
    if(ans==Answer3[3].lower()):
        print(f" The answer is corect you won 5000 ")
        money+=3000
    else:
        print("\nYour answer is wrong ok You won Total Rs",wrong)
        break;
    
    print(questions[3])
    print("\n",Answer4)
    ans,wrong=choice()
    if(ans==Answer4[0].lower()):
        print(f" The answer is corect you won 10000 ")
        money+=5000
    else:
        print("\nYour answer is wrong ok You won Total Rs",wrong)
        break;
    
    print(questions[4])
    print("\n",Answer5)
    ans,wrong=choice()
    if(ans==Answer5[0].lower()):
        print(f" The answer is corect you won 20000 ")
        money+=10000
    else:
        print("\nYour answer is wrong ok You won Total Rs",wrong)
        break;
    
    print(questions[5])
    print("\n",Answer6)
    ans,wrong=choice()
    if(ans==Answer6[0].lower()):
        print(f" The answer is corect you won 50000 ")
        money+=30000
    else:
        print("\nYour answer is wrong ok You won Total Rs",wrong)
        break;

    print(questions[6])
    print("\n",Answer7)
    ans,wrong=choice()
    if(ans==Answer7[1].lower()):
        print(f" The answer is corect you won 100000")
        money+=50000
    else:
        print("\nYour answer is wrong ok You won Total Rs",wrong)
        break;

    print(questions[7])
    print("\n",Answer8)
    ans,wrong=choice()
    if(ans==Answer8[0].lower()):
        print(f" The answer is corect you won 1000000 ")
        money+=900000
    else:
        print("\nYour answer is wrong ok You won Total Rs",wrong)
        break;
    print(f"Congrats{name} You won ",money)
    break
print(f"\n Dhanyaqad {name} ji ")
