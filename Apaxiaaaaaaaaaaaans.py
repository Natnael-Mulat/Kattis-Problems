# https://open.kattis.com/problems/apaxiaaans

text = input()
letter = "imaginary letter"
answer = ""

for i in range(len(text)):
    if letter == text[i]:
        letter = text[i]
    else:
        answer += text[i]
        letter = text[i]
print(answer)