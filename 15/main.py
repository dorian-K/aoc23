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

def hash(s: str):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur = cur % 256
    return cur

assert(len(text) == 1)
text = text[0]
text = text.split(",")
boxes = [[] for i in range(256)]
for ins in text:
    if "=" in ins:
        label, focal = ins.split("=")
        box = boxes[hash(label)]
        
        # find old
        done = False
        for i in range(len(box)):
            if box[i][0] == label:
                # replace
                done = True
                box[i] = (label, focal)
                print("replace")
                break

        if done == False:
            box.append((label, focal))
            print("append, ", hash(label))
    else:
        label = ins[:-1]

        box = boxes[hash(label)]
        
        for i in range(len(box)):
            if box[i][0] == label:
                del box[i]
                print("del")
                break
        
fok = 0
for b in range(len(boxes)):
    box = boxes[b]
    for l in range(len(box)):
        fok += (b + 1) * (l + 1) * int(box[l][1] )
print(fok)
    