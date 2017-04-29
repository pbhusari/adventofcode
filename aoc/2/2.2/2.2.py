w, h = 5, 5
m = [[0 for x in range(w)] for y in range(h)]

X = 'ohp'
A, B, C, D = 'A', 'B', 'C', 'D'
m = [[X, X, 1, X, X],
     [X, 2, 3, 4, X],
     [5, 6, 7, 8, 9],
     [X, A, B, C, X],
     [X, X, D, X, X]]

x = 0
y = 2

foo = open('input.txt', 'r')

##def move(direction):
##    if ((x, y != 1, 1) and (x,y != 0, 2) and (x, y != 2, 0) and (x, y != 1, 3) and (x, y != 2, 4)) and direction == 'L':
##        x -= 1
##    elif ((x, y != 0,2) and (x,y != 3,1) and (x, y != 4,2) and (x, y != 3,3) and (x, y != 2, 4)) and direction == 'R':
##        x+= 1
##    elif ((x, y != 2,0) and (x,y != 3,1) and (x, y != 1,1) and (x, y != 0,2) and (x, y != 4,2)) and direction == 'U':
##        y -= 1
##    elif ((x, y != 1,3) and (x,y != 0, 2) and (x, y != 4,2) and (x, y != 3, 3) and (x, y != 2, 4)) and direction == 'D':
##        y+= 1
##    else:
##        pass

    
for l in foo:
    for direction in l:
        if ((x, y != 1, 1) and (x,y != 0, 2) and (x, y != 2, 0) and (x, y != 1, 3) and (x, y != 2, 4)) and (direction == 'L'):
            x -= 1
        elif ((x, y != 0,2) and (x,y != 3,1) and (x, y != 4,2) and (x, y != 3,3) and (x, y != 2, 4)) and (direction == 'R'):
            x+= 1
        elif ((x, y != 2,0) and (x,y != 3,1) and (x, y != 1,1) and (x, y != 0,2) and (x, y != 4,2)) and (direction == 'U'):
            y -= 1
        elif ((x, y != 1,3) and (x,y != 0, 2) and (x, y != 4,2) and (x, y != 3, 3) and (x, y != 2, 4)) and (direction == 'D'):
            y+= 1
        else:
            pass

    print(m[y][x])
