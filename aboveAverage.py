# https://open.kattis.com/problems/aboveaverage

length = input()

for i in range(int(length)):
    
    grades = input()
    lis = grades.split(" ")
    lis = lis[1:]
    total = 0
    
    for i in range(len(lis)):
         total += int(lis[i])
    average = total/len(lis)

    total1 = 0
    for i in range(len(lis)):
        if int(lis[i]) > average:
                total1+=1
                
    '%.2f' % 5.0
    answer = '%.3f'%((total1/len(lis))*100)
    print(str(answer)+"%")

