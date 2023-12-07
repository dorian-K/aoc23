import re
import numpy
import functools

mint = lambda t: re.search("[0-9]+", t)
def ints(x: str):
    m = re.findall("[0-9]+", x)
    m = [int(x) for x in m]
    return m

f = open("input.txt", "r")
text = f.readlines()

for line in text:
    line = line.strip()