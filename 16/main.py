import re
import numpy
import functools
import math

mint = lambda t: re.search("-?[0-9]+", t)
def ints(x: str):
    m = re.findall("-?[0-9]+", x)
    m = [int(x) for x in m]
    return m

def tr_str(grid: list):
    assert len(grid) > 0
    for i in range(1, len(grid)):
        assert len(grid[i]) == len(grid[0])
        
    tr = [[] for i in range(len(grid[0]))]
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            tr[i].append(grid[j][i])
    return tr

f = open("input.txt", "r")
text = f.readlines()
text = [x.strip() for x in text]
text = [list(x) for x in text]


def get_energy(text, startbeam):
    beams = []
    #row, col
    beams.append(startbeam)

    energized = [[[0] * 4 for i in range(len(text[0]))] for x in range(len(text))]

    #print(energized)

    for iter in range(100000):
        newbeams = []
        if len(beams) == 0:
            break
        # print(len(beams))
        # print(beams)
        for c, dir in beams:
            if c[0] < 0 or c[0] >= len(text):
                continue
            if c[1] < 0 or c[1] >= len(text[c[0]]):
                continue
            dirHash = 0
            if dir[0] == 1:
                dirHash = 1
            if dir[1] == 1:
                dirHash = 2
            if dir[1] == -1:
                dirHash = 3
            if energized[c[0]][c[1]][dirHash] == 1:
                continue
            energized[c[0]][c[1]][dirHash] = 1
            b = text[c[0]][c[1]]
            # print(b)
            if b == ".":
                newdir = dir
            elif b == "/":
                if dir[0] == 0:
                    newdir = (-dir[1], 0)
                else:
                    newdir = (0, -dir[0])
            elif b == "\\":
                if dir[0] == 0:
                    newdir = (dir[1], 0)
                else:
                    newdir = (0, dir[0])  
            elif b == "|":
                if dir[1] == 0:
                    newdir = dir
                else:
                    newbeams.append([(c[0] + 1, c[1]), (1, 0)])  
                    newbeams.append([(c[0] - 1, c[1]), (-1, 0)])  
                    continue
            elif b == "-":
                if dir[0] == 0:
                    newdir = dir
                else:
                    newbeams.append([(c[0], c[1] + 1), (0, 1)])  
                    newbeams.append([(c[0], c[1] - 1), (0, -1)]) 
                    continue 
            newbeams.append([(c[0] + newdir[0], c[1] + newdir[1]), newdir])
            
        beams = newbeams
    assert len(beams) == 0
    #energized = [[str(i) for i in x] for x in energized]
    #energized = ["".join(x) for x in energized]
    #print("\n".join(energized))

    energized = [[max(i) for i in x] for x in energized]
    energized = [sum(x) for x in energized]
    return sum(energized)

max_energy = 0
for row in range(len(text)):
    b1 = [(row, 0), (0, 1)]
    b2 = [(row, len(text[0]) - 1), (0, -1)]
    max_energy = max(max_energy, get_energy(text, b1), get_energy(text, b2))

for col in range(len(text[0])):
    b1 = [(0, col), (1, 0)]
    b2 = [(len(text) - 1, col), (-1, 0)]
    max_energy = max(max_energy, get_energy(text, b1), get_energy(text, b2))

print(max_energy)