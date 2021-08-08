# https://open.kattis.com/problems/addingwords

import sys
dictionary = {'operations' : ["+","-","*","/"]}

def addingWords(words):
    
    word = ''
    test = ''
    
    for i in range(len(words)):
        if (words[i] in dictionary['operations'] or words[i] in dictionary.values())== False:
            test = "failed"
        else:
            word += words[i]        
    if test == "failed":
        return "unknown"
    else:
        answer =  eval(word)
        if str(answer) in dictionary.values():
            for key in dictionary:
                if str(answer) == dictionary[key]:
                    return str(key)
        else:
            return "unknown"

    
for line in sys.stdin:
    
    data = line.split(" ")
    answer = 0
    if data[0].rstrip("\n") == 'clear':
        dictionary.clear()
        dictionary['operations'] = ["+","-","*","/"]
        
    if data[0] == 'def':
        dictionary[data[1]] = (data[2].rstrip("\n"))
        
    if data[0] == 'calc':
        total = []
        for i in range(1,len(data[1:])):
            if data[i] in dictionary :
                total.append(dictionary[data[i]])
            elif data[i] in dictionary['operations']:
                total.append(data[i])
            else:
                total.append(data[i])
        final = ""
        for i in range(1,len(data[1:])+1):
            final += data[i].rstrip("\n")+ " "
        final+= addingWords(total)
        
        print(final)
        