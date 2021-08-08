# https://open.kattis.com/problems/aprizenoonecanwin

rules = input().split(" ")
length = int(rules[0])
limit = int(rules[1])
items = input().split(" ")

count = 1

for i in range(length):
    items[i] = int(items[i])
    
items = sorted(items)
for i in range(1,length):
    if (items[i] + items[i-1]) > limit :
        break
    else:
        count+=1
        
print(count)


