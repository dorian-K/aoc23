import re
import numpy

mint = lambda t: re.search("[0-9]+", t)

f = open("input.txt", "r")
text = f.readlines()

for line in text:
    line = line.strip()