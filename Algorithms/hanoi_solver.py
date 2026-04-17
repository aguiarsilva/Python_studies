def hanoi_solver(disks: int):
    rods = [[], [], []]
    #fill the first rod with disks in descending order
    rods[0] = list(range(disks, 0, -1))
    
    moves = []

    def move_disks(n, src, target, temp):
        if n == 1:
            disk = rods[src].pop()
            rods[target].append(disk)
            moves.append([list(rods[0]), list(rods[1]), list(rods[2])])
        else:
            move_disks(n - 1, src, temp, target)
            move_disks(1, src, target, temp)
            move_disks(n - 1, temp, target, src)
    moves.append([list(rods[0]), list(rods[1]), list(rods[2])])

    #Solve the puzzle
    move_disks(disks, 0, 2, 1)

    output = []
    for move in moves:
        line = f"{move[0]} {move[1]} {move[2]}"
        output.append(line)
    return "\n".join(output)
