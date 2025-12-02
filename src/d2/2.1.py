def main():
    with open("C:/Users/nicol/AdventOfCode/inputs/2.txt", "r") as f:
        lines = f.readlines()
    c = 0

    for i in lines:
        for j in range(int(i.split("-")[0]), int(i.split("-")[1]) + 1):     # iterate over each number in the range (inclusive)
            for k in range(0, (len(str(j))//2) + 1):                        # iterate until the number over halfway of the string (string is symmetric)
                if str(j)[:k].__contains__(str(j)[k:]):
                    print(f"The number {j} is made up of repeating digits {str(j)[k:]}") # print valid matches (testing)
                    c += j
            
                
    print(f"\n{c}")
        
    
    
    
if __name__ == "__main__":
    main()