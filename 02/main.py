import re
import numpy

f = open("input.txt", "r")
text = f.readlines()

number = 0

for line in text:
    line = line.strip()
    if len(line) == 0:
        continue

    idMatch = re.search("[0-9]+", line)
    id = int(idMatch.group())

    line = line[idMatch.end() + 2:]
    line = line.split("; ")
    # gamePossible = True

    min_set = { "red": 0, "green": 0, "blue": 0 }
    for sets in line:
        cols = sets.split(", ")
        for col in cols:
            # print(col)
            num, color = col.split(" ")
            num = int(num)
            if min_set[color] < num:
                min_set[color] = num

    #print(line, gamePossible)
    number += numpy.product(list(min_set.values()))

print(number)