import re
import numpy

f = open("input.txt", "r")
text = f.readlines()
lines = len(text)

gears = set()

def test(line, col):
    if line < 0 or col < 0:
        return None
    if line >= lines or len(text[line]) <= col:
        return None
    
    # orig = (line, col)
    
    if not str.isdecimal(text[line][col]):
        return None
    
    while col >= 0 and str.isdecimal(text[line][col]):
        col -= 1

    #if (line, col + 1) == (0, 81):
    #    print(orig)
    # numbers.add((line, col + 1))
    return (line, col + 1)

for i in range(lines):
    line = text[i].strip()

    for j in range(len(line)):
        if line[j] == '.' or str.isdecimal(line[j]):
            continue
        
        numbers = set()
        # symbol
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                ret = test(i + x, j + y)
                if ret is not None:
                    numbers.add(ret)
        if len(numbers) == 2:
            l = list(numbers)
            gears.add((l[0], l[1]))

sum = 0

counts = {}

for gearList in gears:
    g1 = gearList[0]
    g2 = gearList[1]


    mat = re.search("[0-9]+", text[g1[0]][g1[1]:])
    mat2 = re.search("[0-9]+", text[g2[0]][g2[1]:])
    sum += int(mat.group()) * int(mat2.group())

    '''if mat.group() not in counts:
        counts[mat.group()] = 1
    else:
        counts[mat.group()] += 1
    # print(mat.group())'''

'''
for line in text:
    matches = re.findall("[0-9]+", line)
    for m in matches:
        if m in counts:
            counts[m] -= 1
 
for (key, val) in counts.items():
    if val > 0:
        print((key, val))
'''
print(sum)