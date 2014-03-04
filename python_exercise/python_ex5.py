#!/usr/bin/env python

print "######################################################################"
print "Python practice #5 25 November 2013"
print ""
print "Written by Daniel Yoo"

print "++++++++++++++++++++++++++++++"
###Reading file "test"

b = open("test3", "r")
c = open("test4", "w")
lines = b.readlines()

for line in lines:
	print line,
	words = line.split()
	data1 = [words[0], words[2]]
	for item in data1:
		c.write("%s " % item)
	c.write("\n")
		
b.close()
c.close()
print "++++++++++++++++++++++++++++++"

import subprocess
subprocess.call("/Users/suhyun/util_comp_sci/python/collect_columns_bash", shell=True)








print "######################################################################"