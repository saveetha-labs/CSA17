def solve_puzzle(puzzle):
    goal=[1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    def print_puzzle(p):
        for i in range(0, 9, 3):
            print(p[i:i+3])
            
    print("Initial puzzle state:")
    print_puzzle(puzzle)
    
    while puzzle != goal:
        position=puzzle.index(0)
        
        if position%3 < 2:
            puzzle[position], puzzle[position+1]=puzzle[position+1], puzzle[position]
            
        elif position < 6:
            puzzle[position], puzzle[position+3]=puzzle[position+3], puzzle[position]
            
        print("Current puzzle state:")
        print_puzzle(puzzle)
    print("Solved puzzle state:")
    print_puzzle(puzzle)
    
puzzle=[1, 2, 3, 4, 0, 5, 7, 8, 6]
solve_puzzle(puzzle)
