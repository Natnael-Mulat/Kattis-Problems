# https://open.kattis.com/problems/battlesimulation

attack = input()
comb = ["RBL","RLB","BRL","BLR","LBR","LRB"]
i = 0

while (i<len(attack)):
    if (i<len(attack)-2):
        if (attack[i]+attack[i+1]+attack[i+2]) in comb:
            print("C",end='')
            i+=3
            continue
    i+=1        
    if attack[i] == "R":
        print("S",end='')
    elif attack[i] == "B":
        print("K",end='')
    elif attack[i] == "L":
        print("H",end='')

    
