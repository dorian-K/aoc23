import re
import numpy
import functools
import math

mint = lambda t: re.search("-?[0-9]+", t)
def ints(x: str):
    m = re.findall("-?[0-9]+", x)
    m = [int(x) for x in m]
    return m

f = open("input.txt", "r")
text = f.readlines()

cur_grid = []

def is_horiz(grid: list, row: int):
    num_mismatch = 0
    for i in range(min(row, len(grid) - row)):
        r1 = grid[row - (i + 1)]
        r2 = grid[row + (i)]
        #print("cmp", i, row)
        #print(r1)
        #print(r2)
        for l, r in zip(r1, r2):
            if l != r:
                num_mismatch += 1
                if num_mismatch >= 2:
                    return num_mismatch
    return num_mismatch

def proc(grid: list):
    print("procprocprocprocprocproc")
    num = 0
    for i in range(1, len(grid)):
        if is_horiz(grid, i) != 1:
            continue
        num += 100 * i
        break
    # transpose
    tr = [[] for i in range(len(grid[0]))]
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            tr[i].append(grid[j][i])
    tr = ["".join(x) for x in tr]
    print("saiwtssdadsadsad")
    for i in range(1, len(tr)):
        if is_horiz(tr, i) != 1:
            continue
        assert num == 0
        num += i
        break

    if num == 0:
        print("++++++++++")
        print("\n".join(tr))
        assert False
    return num


total = 0
for line in text:
    line = line.strip()
    if len(line) == 0:
        total += proc(cur_grid)
        cur_grid = []
    else:
        cur_grid.append(line)

if len(cur_grid) > 0:
    total += proc(cur_grid)
print(total)