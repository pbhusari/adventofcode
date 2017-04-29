w, h = 3, 3
m = [[0 for x in range(w)] for y in range(h)]

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

position_origin = m[1][1]
position = m[1][1]

x = 1
y = 1

foo = open('input.txt', 'r')


for l in foo:
    for char in l:
        if (char == 'R') and (x != 2):
            x += 1
        if (char == 'L') and (x != 0):
            x -= 1
        if (char == 'U') and (y != 0):
            y -= 1
        if (char == 'D') and (y != 2):
            y += 1
        else:
            pass
    print( m[y][x] )
            
    
