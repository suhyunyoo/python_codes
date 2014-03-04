#!/usr/bin/env python

import sys
import time

print "######################################################################"
print "Python practice #2 24 November 2013"
print ""
print "Hello World"

def countdown(n):
	print "Counting down"
	while n > 0:
		yield n
		n -= 1

for a in countdown(5):
	print a



def tail(f):
	f.seek(0,2)
	while True:
		line = f.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

def grep(lines, searchtext):
	for line in lines:
		if searchtext in line: yield line



aa = tail(open("outmol"))
print aa

def print_matches(matchtext):
	print "Looking for", matchtext
	while True:
		line = (yield)
		if matchtext in line:
			print line

import div
a, b = div.divide(2305,29)			
print a, b

import div as foo
a, b = foo.divide(1000,40)
print a, b

from div import divide
a, b = divide(2904,12)
print a, b

#pylines = grep(aa,"time")

#for line in pylines:
#	print line,

def fact(n):
	"This function computes a factorial"
	if (n <= 1): return 1
	else: return n * fact(n-1)
	

a = fact(5)
print a
print fact.__doc__

import re



print "######################################################################"