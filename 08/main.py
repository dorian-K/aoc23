import re
import numpy
import functools
import math

mint = lambda t: re.search("[0-9]+", t)
def ints(x: str):
	m = re.findall("[0-9]+", x)
	m = [int(x) for x in m]
	return m

f = open("input.txt", "r")
text = f.readlines()
instructions = text[0].strip()
text = text[2:]

directions = {}

for line in text:
	line = line.strip()
	parsed = re.search("([A-Z1-9]+) = "+re.escape("(")+"([A-Z1-9]+), ([A-Z1-9]+)" + re.escape(")"), line)
	if parsed == None:
		print(line)
	else:
		directions[parsed.group(1)] = (parsed.group(2), parsed.group(3))
		
startNodes = []
# find start nodes
for node in directions.keys():
	if node[-1] == "A":
		startNodes.append(node)

def hasEnded(cur):
	for nod in cur:
		if nod[-1] != "Z":
			return False
	return True

print(startNodes)

cycles = {}

instructions = [0 if x == "L" else 1 for x in instructions]

pairs = []

for node in startNodes:
	steps = 0
	curNode = node
	cycle = []
	fullCycle = []
	cycleStarts = []
	while curNode not in cycle:
		cycle.append(curNode)
		for step in range(len(instructions)):
			fullCycle.append(curNode)
			dir = instructions[step]
			curNode = directions[curNode][dir]

		steps += 1
		
	#print(node, curNode, steps)
	#print(cycle)

	zykelLang = len(fullCycle) - fullCycle.index(curNode)

	if zykelLang % len(instructions) != 0:
		print("wierd", zykelLang % len(instructions), len(instructions))

	indZ = [1 if x[-1] == "Z" else 0 for x in fullCycle].index(1)
	pairs.append((indZ, zykelLang))
	#kgv = int(kgv * len(fullCycle) / math.gcd(kgv, len(fullCycle)))
	
# a + k*b = c + k*d
# a - c + k*(b - d) = 0
# k = (c - a) / (b - d)

print(pairs)

first = pairs.pop()

i = 0
while True:
	m = first[0] + i * first[1]
	matched = True
	# try to match all others
	for pair in pairs:
		r = m - pair[0]
		if r % pair[1] != 0:
			matched = False
			break
	if matched == True:
		print(m)
		for pair in pairs:
			r = m - pair[0]
			kk =  r // pair[1] 
			print(pair[0] + kk * pair[1])

		break
	i += 1
print(i, first[0] + i * first[1])

	