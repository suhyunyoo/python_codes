#!/usr/bin/env python

print "######################################################################"
print "Python practice #6 25 November 2013"
print ""
print "Written by Daniel Yoo"

print "++++++++++++++++++++++++++++++"
###grep in python
e = input("word to be found: ")
b = open("test5", "r")
lines = b.readlines()
d = 5
for i, line in enumerate(lines):
	if e in line:
		c = i 
		for a in range(c,c+d):
			print(lines[a]),
		
b.close()

print "++++++++++++++++++++++++++++++"


print "######################################################################"