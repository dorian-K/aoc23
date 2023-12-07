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

hands = []

for line in text:
	line = line.strip()
	line = line.split(" ")
	hands.append((line[0], int(line[1])))
	
# print(hands)

def recurse(h: list):
	if len(h) == 5:
		return getType_(h)
	
	highest = 0

	for c in strength:
		h.append(c)
		highest = max(highest, recurse(h))
		h.pop()
	
	return highest

def getType(hand: str):
	ls = list(hand)
	
	numJoker = sum(1 for e in filter(lambda x: x == "J", ls))
	ls = list(filter(lambda x: x != "J", ls))

	if numJoker == 5 or numJoker == 4:
		return 6
	
	if numJoker == 0:
		return getType_(ls)
	
	return recurse(ls)
	

def getType_(ls: list):
	counts = []

	while len(ls) > 0:
		character = ls[0]
		count = sum(1 for e in filter(lambda x: x == character, ls))
		counts.append([count, character])

		ls = list(filter(lambda x: x != character, ls))

	counts.sort(key=lambda x: x[0], reverse=True)

	if counts[0][0] == 5:
		return 6
	if counts[0][0] == 4:
		return 5
	
	if counts[0][0] == 3 and counts[1][0] == 2:
		return 4
	if counts[0][0] == 3 and counts[1][0] == 1:
		return 3
	if counts[0][0] == 2 and counts[1][0] == 2:
		return 2
	if counts[0][0] == 2 and counts[1][0] == 1:
		return 1
	
	return 0
	
strength = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")

def compChar(c1, c2):
	i1 = strength.index(c1)
	i2 = strength.index(c2)
	return i1 - i2
	
def comp(hand1, hand2):
	t1 = getType(hand1[0])
	t2 = getType(hand2[0])

	if t2 < t1:
		return -1
	if t1 < t2:
		return 1
	
	for i in range(len(hand1[0])):
		cmp = compChar(hand1[0][i], hand2[0][i])
		if cmp == 0:
			continue
		return cmp
	
	return 0

hands.sort(key=functools.cmp_to_key(comp), reverse=True)

total = 0
for i in range(len(hands)):
	total += hands[i][1] * (i + 1)

print(total)