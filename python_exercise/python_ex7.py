#!/usr/bin/env python
import os

print "######################################################################"
print "Python practice #7 26 November 2013"
print "Written by Daniel Yoo"
print ""

##Find current working directory
str1=os.getcwd()
str2=str1.split('/')
n=len(str2)

path=str2[n-1]
print path

##Find fermi energy and prep DOS source
a = open("outmol", "r")
lines = a.readlines()
for line in lines:
	if "Fermi" in line:
		Ef=line.split()
		Ef=Ef[4]
		EfeV= float(Ef) * 27.211396132
		Efigor= "%5.2f" % EfeV
		print ("Fermi level in eV :"),
		print EfeV
		print Efigor
a.close()

##Total DOS title
b = open("TDOS_"+path, "w")
b.write('{} {}\n'.format("E_"+path, "TD_"+path))
b.close()

##Total DOS title in PDOS data
c = open("DOS_"+path, "w")
lines=[]
lines.append('{} {}'.format("E_"+path, "TD_"+path))
c.writelines(lines)
c.close()

#import subprocess
#subprocess.call("grep -A502 DOS outmol >TDOS", shell=True)



d = open("outmol", "r")
e = open("TDOS", "w")
lines2 = d.readlines()
for i, line in enumerate(lines2):
	if "DOS" in line:
		c = i 
		for l in range(c+1,c+502):
			lines=[]
			lines3=lines2.split()
			print lines3
#			lines.append('{}'.format(lines2[l]))
#			e.writelines(lines)
#e.writelines((lines)

d.close()
e.close()		









print "######################################################################"