length = int(input())

for i in range(length):
    customers = int(input())
    lis = []

    for j in range(customers):
        wood = input().split(" ")
        wood = wood[1:]
        
        size = 0
        for k in range(len(wood)):
            size+= int(wood[k])
        
        lis.append(size)

    lis = sorted(lis)
    time = lis[0]

    for i in range(1,len(lis)):
        lis[i] = lis[i] + lis[i-1]
        time+=lis[i]
        
    time = float(time/customers)

    print(round(time,6))
