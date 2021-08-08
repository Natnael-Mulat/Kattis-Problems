length = int(input())
ballons = input()
ballons = ballons.replace(" ", '')
lis = []
count = 1


for i in range(length):
    if ballons[i] != " ":
        lis.append(int(ballons[i]))

current = max(lis)
index = lis.index(current)

while(lis!=[]):
    for i in range(len(lis)):
        if lis[index] == current and i>=index:
            index = lis.index(current)
            lis.pop(i)
            index-=1
            current -=1
            print(lis)
        else:
            current = max(lis)
            index = ballons.index(str(current))
            count+=1
print(count)
