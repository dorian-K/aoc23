import re
import numpy

mint = lambda t: re.search("[0-9]+", t)

f = open("input.txt", "r")
text = f.readlines()

def parse(nums):
    nums = nums.split(" ")
    nums = filter(lambda x: len(x) > 0, nums)
    nums = map(lambda n: int(n), nums)
    return list(nums)

total = 0
cards = {}

for i in range(1, 206):
    cards[i] = 1

for line in text:
    line = line.strip()
    num = mint(line)
    cardNumber = int(num.group())
    line = line[num.end()+2:]

    '''if not cardNumber in cards:
        cards[cardNumber] = 1
    else:
        cards[cardNumber] += 1'''
    
    line = line.split(" | ")
    winning, my = parse(line[0]), parse(line[1])
    
    numWon = 0
    
    for n in my:
        if n in winning:
            numWon += 1

    # print(cardNumber, ": have", cards[cardNumber], ": won", numWon, )
    
    for i in range(0, numWon):
        cards[cardNumber + i + 1] += cards[cardNumber]

for i in cards.values():
    total += i

print(total)

