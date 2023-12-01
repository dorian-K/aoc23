import re

f = open("input.txt", "r")
text = f.readlines()

#text = ["eightwothree"]

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

calib = 0
for line in text:
	line = line.strip()
	res = [(line.index(x), numbers.index(x) + 1) for x in numbers if x in line]
	if len(res) > 0:
		firstWord = min(res, key=lambda x: x[0])
	else:
		firstWord = (len(line) + 1, 0)
	firstDigit = re.search("[1-9]", line)
	
	if firstDigit != None and firstDigit.start() < firstWord[0]:
		firstDigit = int(line[firstDigit.start()])
	else:
		firstDigit = firstWord[1]

	res = [(line.rfind(x), numbers.index(x) + 1) for x in numbers if x in line]
	if len(res) > 0:
		lastWord = max(res, key=lambda x: x[0])
	else:
		lastWord = (-1, 0)
	lastDigit = re.search("[1-9]", line[::-1])

	if  lastDigit != None and (len(line) - lastDigit.start()) > lastWord[0]:
		lastDigit = int(line[::-1][lastDigit.start()])
	else:
		lastDigit = lastWord[1]
	
	calib += firstDigit * 10 + lastDigit
	print(line, firstDigit * 10 + lastDigit)
		
print(calib)