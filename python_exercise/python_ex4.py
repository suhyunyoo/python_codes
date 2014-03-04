#!/usr/bin/env python

print "######################################################################"
print "Python practice #4 24 November 2013"
print ""
print "Hello World"

print "++++++++++++++++++++++++++++++"
###Reading file "test"
a = open("test", "r")

while 1:
	line = a.readline()
	if not line: break
	print(line),

a.close()

b = open("CONTCAR", "r")
lines = b.readlines()

for line in lines:
	if "S" in line: break
	print(line),

b.close()

for c in range(1,100):
	print c,
	s = []
#	s.append[c*1, c*10, c*30]
	s.append(c*13)
print s
print "++++++++++++++++++++++++++++++"







print "######################################################################"