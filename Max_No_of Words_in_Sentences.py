# . Maximum Number of Words Found in Sentences
sentences=["alice and bob love leetcode", "i think so too fhjghdfj fhsgdjf",
           "this is great thanks very muchgds hd shk",""]
print(sentences)

maximum=0
for sentence in sentences:
    if(sentence==""):
        words=0
    else:
        words=0
    for ch in i:
        if(ch==" "):
            words=words+1
    if(maximum<words):
        maximum=words
print(maximum)
        
    
