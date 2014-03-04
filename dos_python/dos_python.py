#!/usr/bin/python

###The python code for spliting and summation of density of state for VASP output file
###Written by Su-Hyun Yoo
###Last update: 3 March 2014
###Needed input: CONTCAR, DOSCAR, OUTCAR
###Used library: os, sh_vasp, sh_common, math, mathplotlib.pyplot

import os
import sh_vasp as vasp
import sh_common as common
import math
import matplotlib.pyplot as plt

##calculate elapsed time1
start_time = common.get_start_time()

##Find current working directory
path = os.getcwd().split('/')[-1]
print "Current path : " + os.getcwd() +"\n"

##FERMI level check
FERMI = float(vasp.get_keyword_outcar('E-fermi'))
##ISPIN check
ISPIN = vasp.check_ispin_outcar()
##LSORBIT check
LSORBIT = vasp.check_lsorbit_outcar()
##f orbital check
FORBITAL = vasp.check_forbital_outcar(ISPIN, LSORBIT)

print "FERMI :", FERMI, "eV // ISPIN =", ISPIN, "// LSORBIT =", LSORBIT, "// FORBITAL =", FORBITAL

###split_dos
vasp.split_DOSCAR(vasp.get_number_of_each_atom(), vasp.get_sort_of_atoms(), ISPIN, FORBITAL, LSORBIT)

###sum_dos
for a in range(len(vasp.get_sort_of_atoms())):
	vasp.sum_DOSCAR(vasp.get_sort_of_atoms()[a], 1, int(vasp.get_number_of_each_atom()[a]), ISPIN, LSORBIT, FORBITAL)

##make each array for x and y axis from src file
x1 = []
y1 = []
src = open('tDOS', 'r')
lines = src.readlines()
for n, line in enumerate(lines):
	list_line = line.split(" ")
	x1.append(list_line[0])
	y1.append(list_line[1])

##plot using matplotlib
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.set_xlim(float(x1[0]),float(x1[-1]))
plt.show()

##calculate elapsed time2
common.get_elapsed_time(start_time)