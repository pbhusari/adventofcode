import re, math

puzzleinput = "L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2"

position=[0, 0]
face = 0 # along y axis, incrementing goes cw
dpos = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}

position_stack = [position[:]]; ans2_found = False

for rawinst in puzzleinput.strip().split(', '):
    rotation = rawinst[0]
    distance = int(rawinst[1:])
    if rotation == 'R':
        face = (face + 1)%4
    if rotation == 'L':
        face = (face - 1)%4
    
    for _ in range(distance):
        position[0] += dpos[face][0]
        position[1] += dpos[face][1]
        
        if position in position_stack and not ans2_found:
            print("answer 2: manhattan dist to first dupe = {}".format(sum(map(abs, position))))
            ans2_found = True
        
        position_stack.append(position[:])

print("answer 1: final manhattan dist = {}".format(sum(map(abs, position))))
