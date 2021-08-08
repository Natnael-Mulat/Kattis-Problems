# https://open.kattis.com/problems/tripletexting

text = input()
length = len(text)
cut = length//3
words = []
for i in range(0,length,cut):
    words.append(text[i:cut+i])
    
if words[1] == words[2] or words[1] == words[0] :
    print(words[1])
elif words[0] == words[1] or words[0] == words[2]:
    print(words[0])