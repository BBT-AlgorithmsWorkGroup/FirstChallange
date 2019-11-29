def persistance(num):
    times = 0

    while times == 0 or num >= 10:
        digits = 1
        
        prenum = num
        '''while prenum > 0:
            digits = digits*(prenum%10)
            prenum = prenum//10'''
        
        for i in range(1, len(str(num))+1):
            digits =  digits * ((num%10**i)//10**(i-1))

        num = digits
        times += 1 
    
    return times
    
print(persistance(999))
