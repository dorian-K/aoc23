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

grid = [t.strip() for t in text]
startPos = ()

# Find S
for r in range(len(grid)):
	row = grid[r]
	ind = row.find("S")
	if ind == -1:
		continue
	
	startPos = (r, int(ind))
	break

def connPoints(val):
	if val == "|":
		return [(1, 0), (-1, 0)]
	if val == "-":
		return [(0, 1), (0, -1)]
	if val == "L":
		return [(-1, 0), (0, 1)]
	if val == "J":
		return [(-1, 0), (0, -1)]
	if val == "7":
		return [(1, 0), (0, -1)]
	if val == "F":
		return [(1, 0), (0, 1)]
	if val == ".":
		return []
	if val == "S":
		return [(1, 0), (-1, 0), (0, 1), (0, -1)]
	print(val)
	assert False

visited = [[-1] * len(grid[0]) for i in range(len(grid))]
insideOut = [[0] * len(grid[0]) for i in range(len(grid))]

def findAdj(pos):
	global grid, visited
	(r, c) = pos
	val = grid[r][c]
	cp = connPoints(val)
	ret = []
	for (r_rel, c_rel) in cp:
		rr = r + r_rel
		cc = c + c_rel
		if rr < 0 or rr >= len(grid):
			continue
		
		if cc < 0 or cc >= len(grid[rr]):
			continue
		if visited[rr][cc] != -1:
			continue

		nextCp = connPoints(grid[rr][cc])
		if not (-r_rel, -c_rel) in nextCp:
			continue # not connected to us
		ret.append((rr, cc))
	return ret


progress = [startPos]
iter = 0
while len(progress) > 0:
	nextProg = []
	for (r, c) in progress:
		if visited[r][c] != -1:
			continue
		visited[r][c] = iter
		adj = findAdj((r, c))
		if len(adj) == 0:
			continue
		(rr, cc) = adj[0]
		if (rr, cc) in progress or (rr, cc) in nextProg:
			continue
		nextProg.append((rr, cc))
		
		left = []
		right = []
		delta = (rr - r, cc - c)
		next_val = grid[rr][cc]
		if next_val == "|":
			# assume up
			left.append((rr, cc - 1))
			right.append((rr, cc + 1))
			if delta[0] > 0: # down
				left, right = right, left
		if next_val == "-":
			# assume right
			left.append((rr - 1, cc))
			right.append((rr + 1, cc))
			if delta[1] < 0:
				left, right = right, left
		if next_val == "L":
			# assume down
			right.append((rr, cc - 1))
			right.append((rr + 1, cc))
			if delta[1] < 0: # left
				left, right = right, left
		if next_val == "J":
			## assume down
			left.append((rr, cc + 1))
			left.append((rr + 1, cc))
			if delta[1] > 0: #right
				left, right = right, left
		if next_val == "7":
			# assume right
			left.append((rr - 1, cc))
			left.append((rr, cc + 1))
			if delta[0] < 0: # up
				left, right = right, left

		for (rrr, ccc) in left:
			if rrr < 0 or rrr >= len(grid):
				continue
		
			if ccc < 0 or ccc >= len(grid[rr]):
				continue
			if grid[rrr][ccc] != ".":
				continue
			insideOut[rrr][ccc] = 1
		for (rrr, ccc) in right:
			if rrr < 0 or rrr >= len(grid):
				continue
		
			if ccc < 0 or ccc >= len(grid[rr]):
				continue
			if grid[rrr][ccc] != ".":
				continue
			insideOut[rrr][ccc] = 2

	progress = nextProg
	iter += 1

			
# print(iter - 1)

vv = [["#" if x > -1 else " " for x in row] for row in visited]
'''for r in range(len(vv)):
	for c in range(len(vv[r])):
		if vv[r][c] != "#":
			continue
		vv[r][c] = grid[r][c]'''
#for row in insideOut:
#	print("".join([str(x) for x in row]))

def grow(pos):
	global vv
	
	num = 1
	val = vv[pos[0]][pos[1]]
	progress = [pos]
	while len(progress) > 0:
		newProg = []
		for (r, c) in progress:
			for (r_rel, c_rel) in [(1,0), (-1, 0), (0, 1), (0, -1)]:
				rr = r + r_rel
				cc = c + c_rel
				if rr < 0 or rr >= len(vv):
					continue
				
				if cc < 0 or cc >= len(vv[rr]):
					continue
				if vv[rr][cc] != " ":
					assert vv[rr][cc] == "#" or vv[rr][cc] == val, f"{vv[rr][cc]}, {val}"
					continue
				if (rr, cc) in progress or (rr, cc) in newProg:
					continue
				num += 1
				vv[rr][cc] = val
				newProg.append((rr, cc))
		progress = newProg
	return num



growTargets = []
for r in range(len(insideOut)):
	for c in range(len(insideOut[r])):
		if insideOut[r][c] != 0:
			growTargets.append((r, c))
			vv[r][c] = insideOut[r][c]

areaSizes = [0, 0, 0]

for (r, c) in growTargets:
	num = grow((r, c))
	areaSizes[vv[r][c]] += num
	#print("Area:", num)

for a in areaSizes:
	print("Area", a)

for r in range(len(vv)):
	for c in range(len(vv[r])):
		if vv[r][c] == " ":
			print((r, c))
# print("Num area:", cur_val)