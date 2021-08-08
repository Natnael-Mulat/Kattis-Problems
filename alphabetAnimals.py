# https://open.kattis.com/problems/alphabetanimals

possible_answers = []
text = input()
last_letter = text[-1]
length = input()
test = False
animals = [False for i in range(26)]
a = ord('a')

for _ in range(int(length)):
    text = input()
    animals[ord(text[0]) - a] = True
    if last_letter == text[0]:
        possible_answers.append(text)
        
length_possible = len(possible_answers) 
if length_possible == 0:
    test=True
    print("?")
    
if length_possible == 1:
    if possible_answers[0][-1]==last_letter:
        print(possible_answers[0]+"!")
        test=True
        
if test == False:
    for animal in possible_answers:
        newLetter = animal[-1]
        if animals[ord(newLetter) - a] == False:
            print(animal + "!")
            test = True
            break
        
if test == False :
    print(possible_answers[0])
