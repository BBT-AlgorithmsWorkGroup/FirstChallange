
def isPangram(n):
    puren = ""
    
    for i in n.lower():
        if i in 'abcdefghijklmnopqrstuvwxyz' and i not in puren:
            puren = puren + i
    
    return len(puren) == 26

        
print(isPangram("Two driven jocks help fax my big quiz.123456789"))
