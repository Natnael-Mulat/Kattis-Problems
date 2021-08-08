# https://open.kattis.com/problems/iforaneye

def abbr(twitt):
    words = twitt.split()
    abbr = {
        'Bee': 'B','bee': 'b','Too': '2','too': '2','To': '2','to': '2', 'Two': '2', 'two': '2',
        'And': '&', 'One': '1', 'Won': '1', 
        'For': '4', 'Bea': 'B','Oh': 'O', 
        'Sea': 'C','sea': 'c', 'See': 'C', 'Owe': 'O',
        'Are': 'R', 'Why': 'Y','You': 'U', 
        'bea': 'b','at': '@', 'be': 'b',
        'oh': 'o', 'At': '@', 'Be': 'B',
        'and': '&',  'won': '1','one': '1',
        'for': '4', 
        'see': 'c', 
        'owe': 'o', 'are': 'r', 'why': 'y','you': 'u', 
        'four': '4',
        'Four': '4','eye': 'i', 'Eye': 'I'}
    
    for key in abbr:
        for word in words:
            index_of_word = words.index(word)
            if key in word:
                if key == word:
                    words[index_of_word] = word.replace(word,abbr[word])
                else:
                    li = word.split()
                    index = word.index(key)
                    length = len(key)
                    words[index_of_word] = word.replace(word[index:index+length],"$"+abbr[key]+"$")
    for i in range(len(words)):
        if "$" in words[i]:
            words[i]=words[i].replace("$",'')
    return " ".join(words)

def main():
    
    for _ in range(int(input())):
        print(abbr(input()))
if __name__ == "__main__":
    main()


