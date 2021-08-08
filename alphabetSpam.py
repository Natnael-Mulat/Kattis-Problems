# https://open.kattis.com/problems/alphabetspam

spam = input()

def alphabetSpam(spam):
    
    whiteSpace = 0
    lowerCase = 0
    upperCase = 0
    symbols = 0
    total = len(spam)
    
    for i in range(total):
        val = ord(spam[i])
        
        if val == 95:
            whiteSpace+=1
            
        elif val in range(97, 123):
            lowerCase+=1
            
        elif val in range(65, 91):
            upperCase+=1
            
        else:
            symbols+=1
    
    print(whiteSpace/total)
    print(lowerCase/total)
    print(upperCase/total)
    print(symbols/total)

alphabetSpam(spam)

    
    
    