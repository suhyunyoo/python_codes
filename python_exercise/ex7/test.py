#!/usr/bin/env python

a=open("atom_list","r")
e=open("outmol","r")
f=open("DOS_ex7","w")
lines_atomlist=a.readlines()
lines_outmol=e.readlines()
for i in range(0,5):
	lines2=lines_atomlist[i]
	lines2=lines2.split()
	Atomname=lines2[2]
	Atomnum=lines2[1]
	f1=open("pDOS_"+Atomname+"_"+Atomnum,"r")
	lines_pdos=f1.readlines()
	for n, line in enumerate(lines_pdos):
		llines=[]
		llines=line.split()
		print llines


a.close()
e.close()
f.close()