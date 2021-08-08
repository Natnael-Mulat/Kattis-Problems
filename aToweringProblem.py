info = input().split(" ")
height1 = int(info[6])
height2 = int(info[7])
info = info[:6]
h1 = []
h2 = []
string1 = ""

for i in range(len(info)):
    test = []
    test1 = []
    for j in range(i+1,len(info)):
        for k in range(j+1,len(info)):
            if (i!=j) and (k!=i) and (k!=j):
                if (int(info[i])+int(info[j])+int(info[k])) == height1:
                    
                    test.append(int(info[i]))
                    string1+=info[i]
                    test.append(int(info[j]))
                    string1+=info[j]
                    test.append(int(info[k]))
                    string1+=info[k]
                    
                if (int(info[i])+int(info[j])+int(info[k])) == height2:
                    if (info[i] not in string1) and (info[j] not in string1) and (info[k] not in string1):
                        test.append(int(info[i]))
                        test.append(int(info[j]))
                        test.append(int(info[k]))
                    
    if test!=[]:
        test = sorted(test)
        test = test[::-1]
        h1.append(test)


# if sum(h1[0]) == height1:
#     print(h1[0][0],end=" ")
#     print(h1[0][1], end= " ")
#     print(h1[0][2], end= " ")
#     print(h1[1][0],end=" ")
#     print(h1[1][1], end= " ")
#     print(h1[1][2])
#     
# else:
#     print(h1[1][0],end=" ")
#     print(h1[1][1], end= " ")
#     print(h1[1][2], end= " ")
#     print(h1[1][0],end=" ")
#     print(h1[1][1], end= " ")
#     print(h1[0][2])
print(h1)