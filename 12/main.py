import re
import numpy
import functools
import math
from z3 import *

mint = lambda t: re.search("-?[0-9]+", t)
def ints(x: str):
	m = re.findall("-?[0-9]+", x)
	m = [int(x) for x in m]
	return m

f = open("input.txt", "r")
text = f.readlines()

patterns = []
for i in range(100):
	if i == 0:
		patterns.append(None)
		continue
	patterns.append(re.compile("(\\.|\\?)+?([?#]{"+str(i)+"})(\\.|\\?)"))

cur_ind = []
total_str = ""
total_conf = ()
cache_expr = None

def magic(t: str, conf: tuple):
	t = list(t)
	max_ind = len(t)
	s = Solver()
	X = BoolVector("x", len(t))
	pre_set = 0
	actually_imp = []
	for i, c in enumerate(t):
		if c == ".":
			s.add(X[i] == False)
		elif c == "#":
			pre_set += 1
			s.add(X[i] == True)
		else:
			actually_imp.append(X[i])

	total_conf = sum(conf)
	
	s.add(Sum([If(xx, 1, 0) for xx in actually_imp]) == total_conf - pre_set)
	#lool = Int("lool")
	#s.add(ForAll(lool, If(Or(lool < 0, lool >= max_ind), Select(X, lool) == 0, True)))

	Ind = IntVector("i", len(conf))
	
	for i, c in enumerate(conf):
		s.add(And(Ind[i] >= 0, Ind[i] < max_ind - c - 1))
		for ind in range(1, max_ind - c - 1):
			cond = []
			for off in range(c):
				cond.append(X[ind + off] == True)
			cond.append(X[ind - 1] == False)
			cond.append(X[ind + c] == False)
			s.add(If(Ind[i] == ind, And(cond), True))
		# bigger than all previous
		if i > 0:
			s.add(Ind[i] > Ind[i - 1])

	for ix, x in enumerate(X):
		# if an X is set, it must be because of an Ind
		impl = []
		for ic, c in enumerate(conf):
			impl.append(And(ix >= Ind[ic], ix < Ind[ic] + c))
		s.add(If(x, Or(impl), True))

	print(s.check())
	combs = 0
	if s.check() == sat:
		
		s.set("timeout", 100)

		def godown(s: z3.Solver, i, X, t):
			
			if i >= len(X):
				res = s.check()
				if res == sat:
					print("saat")
					return 1
				if res == unsat:
					return 0
				assert False
			if t[i] != "?":
				return godown(s, i + 1, X, t)
			print(i)
			comb = 0
			s.push()
			s.add(X[i] == True)
			
			if s.check() != unsat:
				comb += godown(s, i + 1, X, t)
			s.pop()
			s.push()
			s.add(X[i] == False)
			if s.check() != unsat:
				comb += godown(s, i + 1, X, t)
			s.pop()
			return comb
		combs = godown(s, 0, X, t)
	return combs


def is_valid(s: str, conf):
	global total_str, cache_expr
	if cache_expr == None:
		expr = "($|\\.|\\?)*"
		for i in conf:
			expr += "([?#]{"+str(i)+"})($|\\.|\\?)+"
		cache_expr = re.compile(expr)
		#expr += "[.?]*"
	m = re.match(cache_expr, s)
	assert m != None and m.end() == len(s), total_str + " " + str(conf) + " " + s
	
	return m != None and m.end() == len(s)
	#return True

'''loc = list(total_str)
		running = 0
		for (ind, l) in cur_ind:
			for i in range(l):
				assert loc[ind + running + i] == "?" or loc[ind + running + i] == "#" 
				loc[ind + running + i] = "#"
				
			running += ind + l
		
		loc = ["." if x == "?" else x for x in loc]
		# print("".join(loc), cur_ind, total_str)
		if is_valid("".join(loc), total_conf):
			return 1
		return 0'''

@functools.lru_cache(maxsize=100000000)
def numberOfSol(line: str, conf: tuple):
	stack = [0]
	cur_c = 0

	combinations = 0
	while(len(stack) > 0):
		si = stack[-1]
		if len(conf) == cur_c:
			if "#" not in line[si:]:
				combinations += 1
			stack.pop()
			cur_c -= 1
			continue
		
		req = conf[cur_c]
		
		# find consecutive
		m = re.match(patterns[req], line[si:])
		if m == None:
			stack.pop()
			cur_c -= 1
			continue
		stack[-1] += max(1, m.start(2))

		if cur_c == 1:
			combinations += numberOfSol(line[si+m.end(2):], conf[cur_c + 1:])
		else:
			stack.append(si + m.end(2))
			cur_c += 1
		
		if "#" in line[si:si + m.start(2)]:
			stack.pop()
			cur_c -= 1
		
	return combinations



def test(line:str, ind: int):
	global total_str, total_conf, cache_expr
	line = line.strip()
	line = line.split(" ")
	line, conf = line[0], ints(" ".join(line))
	line = "?".join([line] * 5)
	conf = conf * 5
	line = "."+line+"."
	total_str = line
	total_conf = conf
	cache_expr = None
	
	print(ind, line, conf)
	# print(line, conf, numberOfSol(line, conf))
	
	return numberOfSol(line, tuple(conf))
	 
total = 0
for i, line in enumerate(text):#
	total += test(line, i)
	
	
#total = test("??#?#?#????.????#? 6,2,1,1")
print(total)