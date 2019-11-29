
def wRace(words):

    words = words.split()
    score = []
    
    for i in words:
        wTotal = 0
        
        for n in i.lower():
            wTotal = wTotal + (ord(n)-96)
        score = score + [wTotal]
        
    return words[score.index(max(score))]        

print(wRace(input("? ")))
