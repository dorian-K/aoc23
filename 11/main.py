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
text = [x.strip() for x in text]

hexp = [1] * len(text[0])
vexp = [1] * len(text)

for row, line in enumerate(text):
	line = line.strip()
	if "#" not in line:
		vexp[row] = 1000000

for col in range(len(text[0])):
	any = False
	for j in range(len(text)):
		if text[j][col] == '#':
			any = True
			break
	
	if any:
		continue
	hexp[col] = 1000000

indices = []
for row, line in enumerate(text):
	m = re.finditer("#", line)
	m = [(row, i.start()) for i in m]
	indices.extend(m)

for (row, col) in indices:
	assert text[row][col] == "#"

# print(indices)

num = 0
for i in range(len(indices)):
	for j in range(i + 1, len(indices)):
		# print(i, j)

		start = (min(indices[i][0], indices[j][0]), min(indices[i][1], indices[j][1]))
		end = (max(indices[i][0], indices[j][0]), max(indices[i][1], indices[j][1]))
		
		dist = 0
		for y in range(end[0] - start[0]):
			dist += vexp[y + start[0]]
		for x in range(end[1] - start[1]):
			dist += hexp[x + start[1]]
		num += dist
		#print(i+1,j+1,dist)
		#num += (abs(indices[i][0] - indices[j][0]) + abs(indices[i][1] - indices[j][1]))
print(num)