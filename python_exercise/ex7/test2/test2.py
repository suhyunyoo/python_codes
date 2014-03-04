#!/usr/bin/env python

a = open("tDOS","r")
#a = open("pDOS_Br_1","r")
b = open("pDOS_Pd_2","r")
c = open("pDOS_Pd_3","r")
d = open("sum","w")
lines_a=a.readlines()
lines_b=b.readlines()
lines_c=c.readlines()

lines=[]

for i, e in enumerate(lines_a):
	lines_a[i] = lines_a[i].replace('\n',' ')
	lines_b[i] = lines_b[i].replace('\n',' ')
	lines_c[i] = lines_c[i].replace('\n',' ')
	aa=[lines_a[i] +lines_b[i] +lines_c[i] + "\n"]
	lines.append(aa)
	#print lines[i]
	d.writelines(lines[i])
	print e


a.close()
b.close()
c.close()
d.close()