def main():
    with open("C:/Users/nicol/AdventOfCode/inputs/2.txt", "r") as f:
        lines = f.readlines()
    c = 0

    for i in lines:
        for j in range(int(i.split("-")[0]), int(i.split("-")[1]) + 1):
            for k in range(1, (len(str(j))//2) + 1):
                ss = str(j)[:k]
                                
                if ss*(len(str(j)) // len(ss)) == str(j):                   
                    print(f"The number {j}\t is made up of:\t{str(j)[:k]}")
                    c += j
                    break
                           
    print(f"\n{c}")
        
    
    
    
if __name__ == "__main__":
    main()