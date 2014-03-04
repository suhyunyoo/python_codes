#!/usr/bin/env python


print "###################################"
print "Python practice #1 23 November 2013"
print ""
print "Hello world"
print "The calculation of the compound interest"

principal = 1000
rate = 0.05
numyears = 5
year = 1

while year <= numyears:
  principal = principal * (1 + rate)
  print year, principal
  year += 1

integer = 3
decimal = integer * 0.42

print "%0.1f" % (decimal)

s = "i hate spam"

#if 'spam' in s:
#	has_spam = True
#else:
#	has_spam = False
has_spam = 'spam' in s

print has_spam

#f = open("test")
#line = f.readline()
#while 'clock' in line:
#	print line,
#	line = f.readline()
#f.close()

for line in open("test"):
	print line,

principal = 1000
rate = 0.05
numyears = 5
year = 1

f = open("out","w")
while year <= numyears:
	principal = principal * (1 + rate)
	print >>f, "%3d %0.2f" % (year,principal)
#	print ("%3d %0.2f" % (year,principal),file=f)
	year += 1
f.close()


#import sys
#sys.stdout.write("Enter your first name:")
#name = sys.stdin.readline()
#print name,

#name1 = raw_input("Enter your last name:")
#print name1


print """test1
test2
test3
test4
"""
a = 'hello world1'
b = "hello world2"
c = """hello world3"""
print a, b, c

d = a[4]
print "4th letter in a (hello world1):", d

e = a + b + d + d + "Attachment test"
print e

x = 37
y = 43
print x + y

x = "37"
y = "43"
print x + y + "just using x + y"
print "%10.3f" % (float(x) + float(y))

f = open("CONTCAR")
lines = f.readlines()
print lines
print lines[0],
print lines[1],
print lines[7],
print lines[9],
print lines[9][5]
print len(lines)

fvalues = [float(lines[1])]
print fvalues
#while lines:
#	b = len(lines)
#	print b

#for line in open("CONTCAR"):
#	print line,
#	print len(line)
#for line in open("CONTCAR"):
#	print line,
#	print len(line)

import sys
a = (sys.argv)
print len(a)

print """++++++++++++++++++++++++"""
filename="CONTCAR"
portfolio = []
for line in open(filename):
	print line,
	fields = line.split(",")
	name = fields[0]
print """++++++++++++++++++++++++"""

a = range(50,14,-2)
print a

def remainder(a,b):
	q=a//b
	r=a-q*b
	return (a,b,q,r)

print remainder(3,2)
c, d, e, f = remainder(10,4)
print a, b
print c, d
print """++++++++++++++++++++++++"""

def countdown(n):
	print "Counting Down"
	while n>0:
		yield n
		n -= 1

c = countdown(5)
c.next()

for i in countdown(5):
	print i


print "###################################"