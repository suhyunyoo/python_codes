#!/usr/bin/python
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
ISPIN = int(vasp.get_keyword_outcar('ISPIN'))
if ISPIN == 2: ISPIN = True
else: ISPIN = False

##LSORBIT check
LSORBIT = vasp.get_keyword_outcar("LSORBIT")
if LSORBIT == "T": LSORBIT = True
else: LSORBIT = False

##f orbital check
FORBITAL = False #default
doscar = open('DOSCAR')
for i in range(5): tmp=doscar.readline()
num_line = int(doscar.readline().split()[2])
for i in range(num_line+1): tmp=doscar.readline()
sample_line = doscar.readline().split()
n_pdos = len(sample_line) - 1
if n_pdos == 4 and ISPIN == False:
	FORBITAL = True
	pass
elif n_pdos == 8 and ISPIN == True:
	FORBITAL = True
	pass
elif n_pdos == 12 and ISPIN == False:
	if LSORBIT == True: pass
	else: print "[WARN] Spin-orbit coupling-like configuration is found in your doscar. But LSORBIT is not found in your outcar. Please solve it."
elif n_pdos == 16 and ISPIN == False:
	if LSORBIT == True:
		FORBITAL == True
		pass
	else: print "[WARN] Spin-orbit coupling-like configuration is found in your doscar. But LSORBIT is not found in your outcar. Please solve it."
else: print "Error with your DOSCAR."	
doscar.close

############################################################
#TMP#########################################################
############################################################
#def split_DOSCAR(number_of_each_atom, sort_of_atoms, ISPIN, FORBITAL):
	##Fermi-level
#	FERMI = float(vasp.get_keyword_outcar('E-fermi'))
	##Skipping unnecessary part in DOSCAR
#	doscar = open('DOSCAR')
#	for i in range(5): tmp=doscar.readline()
#	num_line = int(doscar.readline().split()[2])
#	doscar.close

#	doscar = open("DOSCAR", "r")
#	for i in range(6): tmp = doscar.readline()

	#TDOS, considering ISPIN
#	tdos = open("tDOS", "w")
#	for i in range(num_line): 
#		tdos = doscar.readline().split()
#		line = float(tdos[0]) - FERMI, float(tdos[1], tdos[2]
#		tdos.write(line)
#	doscar.readline()

#split_DOSCAR(vasp.get_number_of_each_atom(), vasp.get_sort_of_atoms(), ISPIN, FORBITAL)

############################################################
#TMP#########################################################
############################################################

###split_DOSCAR
vasp.split_DOSCAR(vasp.get_number_of_each_atom(), vasp.get_sort_of_atoms(), ISPIN, FORBITAL)

###sum_dos
for a in range(len(vasp.get_sort_of_atoms())):
	vasp.sum_DOSCAR(vasp.get_sort_of_atoms()[a], 1, int(vasp.get_number_of_each_atom()[a]))
	print vasp.get_sort_of_atoms()[a]
	print vasp.get_number_of_each_atom()[a]

##make each array for x and y axis from src file
x1 = []
y1 = []
src = open('tDOS', 'r')
lines = src.readlines()
for n, line in enumerate(lines):
	list_line = line.split(" ")
	x1.append(list_line[0])
	y1.append(list_line[2])

##plot using matplotlib
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.set_xlim(float(x1[0]),float(x1[-1]))
plt.show()


##calculate elapsed time2
common.get_elapsed_time(start_time)