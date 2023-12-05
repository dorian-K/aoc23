import re
import numpy

mint = lambda t: re.search("[0-9]+", t)

f = open("input.txt", "r")
text = f.readlines()

maps = {}
cur_map = []
cur_map_name = ()
seeds = []

for line in text:
    line = line.strip()
    if "seeds" in line:
        matches = re.findall(" [0-9]+ [0-9+]+", line)
        matches = [m.strip().split(" ") for m in matches]
        seeds = [(int(m[0]), int(m[1])) for m in matches]
    elif "map:" in line:
        if len(cur_map) > 0:
            maps[cur_map_name] = cur_map
            cur_map = []
        m = re.search("([a-z]+)-to-([a-z]+) map", line)
        cur_map_name = (m.group(1), m.group(2))
    else:
        if len(line) < 2:
            continue
        m = re.search("([0-9]+) ([0-9]+) ([0-9]+)", line)
        destStart = int(m.group(1))
        sourceStart = int(m.group(2))
        leng = int(m.group(3))

        cur_map.append((sourceStart, destStart, leng))
if len(cur_map) > 0:
    maps[cur_map_name] = cur_map
    cur_map = {}

ends = []

progress = {}
for (fro, to) in maps.keys():
    if not fro in progress:
        progress[fro] = []

for (start, length) in seeds:
    progress["seed"].append((start, length))
    print((start, length))

changed = True
while changed == True:
    changed = False
    for (fro, to) in maps.keys():

        map = maps[(fro, to)]
        while(len(progress[fro]) > 0):
            changed = True
            (neededStart, neededLen) = progress[fro].pop()

            while neededLen > 0:
                closest = neededLen
                for (sourceStart, destStart, realLen) in map:
                    if neededStart >= sourceStart and neededStart < sourceStart + leng:
                        usedLen = realLen - (sourceStart - neededStart)
                        neededLen -= usedLen
                        progress[to].append((destStart + (sourceStart - neededStart), usedLen))
                        closest = 0
                        break
                    
                    if sourceStart > neededStart:
                        closest = min(closest, sourceStart - neededStart)
                if closest > 0:
                    neededLen -= closest
                    if to == "location":
                        ends.append((neededStart, closest))
                    else:
                        progress[to].append((neededStart, closest))

print(progress)
print(ends)
