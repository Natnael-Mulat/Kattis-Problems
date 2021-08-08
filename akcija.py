length = int(input())
lis = []

for i in range(length):
    lis.append(int(input()))

lis = sorted(lis)
lis = lis[::-1]

min_price = 0
count=1

for i in range(length):
    if count==3:
        count = 1
    else:
        count+=1
        min_price += lis[i]
        

print(min_price)