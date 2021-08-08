# https://open.kattis.com/problems/4thought

operators = ["+","-", "*", "//"]
pairs = ["4 + 4", "4 - 4", "4 * 4", "4 / 4"]

def four_thought(n):
    
    for pair in pairs:
        for operator in operators:
            for another_pair in pairs:
                solu = eval(pair+operator+another_pair)
                if solu == n:
                    return str(pair)+" "+ str(operator)+" "+str(another_pair)
    return ""

def main():
    
    for _ in range(int(input())):
        
        n=int(input())
        solution = four_thought(n)
        if solution == "":
            print("no solution")
        else:
            print(solution.replace("//","/")+" = "+str(n))
        
if __name__ == "__main__":
    main()
