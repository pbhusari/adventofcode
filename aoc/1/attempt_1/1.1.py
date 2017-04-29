import re

fulltext = "L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2"
listtext = fulltext.split(', ')
listtextnumbers = []
xylist = []
vectorlist = []

for item in listtext:
    scalar = int(item[1:])
    if 'L' in item:
        x = -1
        y = 0
    if 'R' in item:
        x = 1
        y = 0
    if 'U' in item:
        x = 0
        y = 1
    if 'D' in item:
        x = 0
        y = -1
    coordinate = (str(str(scalar*x) + ";" + str(scalar*y)))
    xylist.append(str(coordinate))
        
class Vector:
    def __init__(self, mag_x, mag_y):
        self.mag_y = float(mag_y)
        self.mag_x = float(mag_x)

    def __str__(self):
        return "(" + str(self.mag_x) + "," + str(self.mag_y) + ')'

    def __add__(self, other):
        return Vector(self.mag_x + other.mag_y, self.mag_y + other.mag_x)

vector_total = Vector(0, 0)

for item in xylist:
    location = item.find(';')
    xvalue = item[0:location]
    yvalue = item[(location + 1):]
    vector_total += Vector(xvalue, yvalue)

print(vector_total)

    
