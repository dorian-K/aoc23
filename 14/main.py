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
print("\n".join(["".join(x) for x in text]))
print("")

def move_left(text, rev):
    for i in range(len(text)):
        changed = True
        row = text[i]
        if rev:
            row = row[::-1]
        while changed:
            changed = False
            for j in range(len(text[0]) - 1):
                if row[j] == "." and row[j + 1] == "O":
                    row[j], row[j + 1] = row[j + 1], row[j]
                    changed = True
        if rev:
            row = row[::-1]
        text[i] = row
    return text


def cycle(text):
    #assert text == ["".join(x) for x in tr_str(tr_str(text))], str(["".join(x) for x in tr_str(tr_str(text))]) + str(tr_str(tr_str(text)))
    
    text = tr_str(text)
    text = move_left(text, False)
    text = tr_str(text)
    text = move_left(text, False) 
    text = tr_str(text)
    text = move_left(text, True)
    text = tr_str(text)
    text = move_left(text, True) 
       
    #print("\n".join(["".join(x) for x in text]))
    #print("")
        
    return text

cache_cycle = []

for i in range(0, 142):
    if i % 10000 == 0:
        print(i)
    text = cycle(text)

    if text in cache_cycle:
        print("dup!", i)
        print("cycle start", cache_cycle.index(text))
        print("cycle length", i - cache_cycle.index(text))
        break
    cache_cycle.append(text)
    

    # text = ["".join(x) for x in text]
    # print("\n".join(text))

load = 0
for row in range(len(text)):
    for col in range(len(text[row])):
        if text[row][col] == "O":
            load += len(text) - row
print(load)