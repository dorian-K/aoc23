import re
import numpy

f = open("input.txt", "r")
text = f.readlines()

for line in text:
    line = line.strip()