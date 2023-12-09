import re
import numpy
import functools
import math

mint = lambda t: re.search("[0-9]+", t)
def ints(x: str):
    m = re.findall("[0-9]+", x)
    m = [int(x) for x in m]
    return m

def coolInts(x: str):
    m = x.split(" ")
    return [int(x) for x in m]

f = open("input.txt", "r")
text = f.readlines()

total = 0

#for line in text:
def test(line):
    global total 
    line = line.strip()
    i = coolInts(line)
    diffs = [i]
    while(sum([abs(x) for x in diffs[-1]]) != 0):
        arr = [0] * (len(diffs[-1]) - 1)
        for i in range(len(arr)):
            arr[i] = diffs[-1][i + 1] - diffs[-1][i]
        diffs.append(arr)
        # print(arr)
   

    # pred
    diffs[-1].insert(0, 0)
    for i in range(len(diffs) - 1):
        diffs[-(i + 2)].insert(0, diffs[-(i + 2)][0] - diffs[-(i + 1)][0])
        # print(diffs[-(i + 2)][-1])
    
    total += (diffs[0][0])
    # print(diffs[0][-1])

for line in text:
    test(line)

print(total)