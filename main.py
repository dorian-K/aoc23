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

for line in text:
    line = line