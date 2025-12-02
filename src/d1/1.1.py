def main(): 
    with open("C:/Users/nicol/AdventOfCode/inputs/1.txt", "r") as f:
        lines = f.readlines()

    dial = 50     
    z = 0
    
    for i in lines:
        if dial < 0 : dial = dial % 100
        if dial > 99 : dial = dial % 100
        if dial == 0: z+=1
        
        if i[0] == 'L':
            print(f"The dial ({dial}) is rotated left by {int(i[1:])}, it is now {dial + int(i[1:])}")
            dial = dial + int(i[1:])
        elif i[0] == 'R':
            print(f"The dial ({dial}) is rotated right by {int(i[1:])}, it is now {dial - int(i[1:])}")
            dial = dial - int(i[1:])
            
            
       
        
    print(f"{dial}, {z}")   

if __name__ == "__main__":
    main()