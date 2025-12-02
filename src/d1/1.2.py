def main(): 
    with open("C:/Users/nicol/AdventOfCode/inputs/1.txt", "r") as f:
        lines = f.readlines()

    dial = 50     
    z = 0
    
    for i in lines:
        a = 0
        
        if dial < 0 : dial = dial % 100
        if dial > 99 : dial = dial % 100
        if dial == 0: z+=1
        
        if i[0] == 'L':
            print(f"The dial ({dial}) is rotated left by {int(i[1:])}, it is now {dial + int(i[1:])}")
            a += int(i[1:]) // 100; z += int(i[1:]) // 100                                                      # add the quotient of the number of rotations (guaranteed times the dial passed 0)
            
            if (dial < 0 and dial + (int(i[1:]) % 100) > 0) or (dial > 0 and dial + (int(i[1:]) % 100) > 100):  # check if the remainder passed 0 at when added and if so add one to the total
                a += 1; z += 1           

            print(f"The dial ({dial + int(i[1:])}) passed 0 {a} times")
            dial = dial + int(i[1:])
            
        elif i[0] == 'R':
            print(f"The dial ({dial}) is rotated right by {int(i[1:])}, it is now {dial - int(i[1:])}")
            a += int(i[1:]) // 100; z += int(i[1:]) // 100
            
            if (dial < 0 and dial - (int(i[1:]) % 100) < -100) or (dial > 0 and dial - (int(i[1:]) % 100) < 0):
                a += 1; z += 1           
                
            print(f"The dial ({dial - int(i[1:])}) passed 0 {a} times")
            dial = dial - int(i[1:])
            
            
       
        
    print(f"{dial}, {z}")   

if __name__ == "__main__":
    main()
