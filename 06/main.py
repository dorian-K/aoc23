import re
import numpy

mint = lambda t: re.search("[0-9]+", t)
def ints(x: str):
	m = re.findall("[0-9]+", x)
	m = [int(x) for x in m]
	return m

f = open("input.txt", "r")
text = f.readlines()


for line in text:
	line = line.strip()
	if "Time" in line:
		times = ints(line)
	elif "Distance" in line:
		dists = ints(line)
			
total = 1

for (time, dist) in zip(times, dists):
	numWon = 0
	for holdTime in range(time):
		remainingTime = time - holdTime
		newDist = remainingTime * holdTime
		if newDist > dist:
			numWon += 1
	total *= numWon

print(total)

