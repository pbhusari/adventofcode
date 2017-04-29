author = 'PRANAVBHUSARI'
date = '4/28/2017'

w, h = 7, 7
m = [['X' for x in range(w)] for y in range(h)]

A, B, C, D = 'A', 'B', 'C', 'D'

#      0    1    2    3    4    5    6
m = [['X', 'X', 'X', 'X', 'X', 'X', 'X'],   #0
     ['X', 'X', 'X', '1', 'X', 'X', 'X'],   #1
     ['X', 'X', '2', '3', '4', 'X', 'X'],   #2
     ['X', '5', '6', '7', '8', '9', 'X'],   #3
     ['X', 'X', 'A', 'B', 'C', 'X', 'X'],   #4
     ['X', 'X', 'X', 'D', 'X', 'X', 'X'],   #5
     ['X', 'X', 'X', 'X', 'X', 'X', 'X']]   #6

x, y = 1, 3

file1 = open('input.txt', 'r')

def mov_test(m1, x1, y1, direction):
    if direction == 'L':
        x1 -= 1
        if m[y1][x1] == 'X':
            return bool(0)
        else:
            return bool(1)

    elif direction == 'R':
        x1 += 1
        if m1[y1][x1] == 'X':
            return bool(0)
        else:
            return bool(1)

    elif direction == 'U':
        y1 -= 1
        if m1[y1][x1] == 'X':
            return bool(0)
        else:
            return bool(1)

    elif direction == 'D':
        y1 += 1
        if m1[y1][x1] == 'X':
            return bool(0)
        else:
            return bool(1)

    else:
        return bool(0)

for line in file1:
    for char in line:
        if ((char == 'L') and (mov_test(m, x, y, 'L'))):
            x -= 1
        elif ((char == 'R') and (mov_test(m, x, y, 'R'))):
            x += 1
        elif ((char == 'U') and (mov_test(m, x, y, 'U'))):
            y -= 1
        elif ((char == 'D') and (mov_test(m, x, y, 'D'))):
            y += 1
        else:
            pass
    print(m[y][x])

