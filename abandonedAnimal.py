
def abandonedAnimal(lis):
    
    possible = []
    output = []
    
    for i in range(len(lis)):
        copy = lis[i]
        output.append(copy)
        
    while any(output) :
        check = []
        choice = 0
        for i in range(len(output)):
            if output[i]!=[]:
                
                for k in range(len(output[i])):
                    if output[i][k] == choice or output[i][k] > choice:
                        choice = output[i][k] 
                        check.append(choice)
                        output[i] = output[i][k+1:]
                        break
                else:
                    output[i] = output[i][k+1:]
  
        possible.append(check)
        
#     print(possible)
    test = False
    if len(possible)==1:
        if len(possible[0]) != len(lis):
            return "impossible"
        else:
            return "unique"
    
    
    elif len(possible)>1:
        string = ""
        for i in range(len(possible)):
            count1 = 0
            if len(possible[i])==len(lis):
                string = "unique"
            else:
                for j in range(len(possible[i])):
                    for k in range(len(lis)):
                        if possible[i][j] in lis[k]:
#                             print(possible[i][j])
                            count1+=1
                        else:
                            break
            
            
     
    if count1==len(lis) and string == "unique":
        return "ambiguous"
    elif string == "unique":
        return "unique"
    elif string == "":
        return "impossible"
                
    

                    
def main():

    text = input()
    list1 = []
    for i in range(int(text)):
        list1.append([])
        
    text= input()
    for i in range(int(text)):
        text = input()
        list1[int(text[0])].append(str(text[2:]))
    

    text = input()
    lis = []
    length_lis = int(text)
    for _ in range(length_lis):
        text = input()
        track = []
        for j in range(len(list1)):
            if str(text) in list1[j]:
                track.append(j)
        lis.append(track)
        
#     print(lis)
    print(abandonedAnimal(lis))
    
if __name__ == "__main__":
    main()
