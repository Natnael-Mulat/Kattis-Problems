# https://open.kattis.com/problems/airconditioned

minions = int(input())

lis = []
count = 1

for i in range(minions):
    temp = input().split(" ")
    lower = int(temp[0])
    upper = int(temp[1])
    lis.append([upper,lower])

lis = sorted(lis)
limit = lis[0][0]

for i in range(len(lis)):
    if(lis[i][1] > limit) :
        limit = lis[i][0]
        count+=1
        
print(count)