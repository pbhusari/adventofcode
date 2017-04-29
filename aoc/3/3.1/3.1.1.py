file1 = open('test.txt', 'r')
lines = 0

possible_count = 0

#expected input from test: 1+1+1+1 = 4
for line in file1:
    if ('#' in line):
        pass
    else:
        line = line.strip()
        line = line.replace('  ', ':')
        sides = sorted(line.split(':'))

        for item in sides:
            item = int(item)
        
        #print(templist)

        if sum(sides[0:2]) > sides[2]:
                valid_triangle_count += 1
        else:
            pass
        
        lines += 1

print(possible_count)
    
        

    
