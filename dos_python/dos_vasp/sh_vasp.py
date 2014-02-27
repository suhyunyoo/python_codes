#!/usr/bin/python
### Python Library for VASP
### INPUT: CONTCAR, OUTCAR, DOSCAR 
### Last update: 12 February 2014
from copy import deepcopy
import os
path = os.getcwd().split('/')[-1]

###CONTCAR
def get_total_number_of_atoms():
	with open('CONTCAR', 'r') as cont:
		for i in range(6): tmp = cont.readline()
		num_atoms = 0
		a = cont.readline().split()
		for n in range(len(a)):
			num_atoms += int(a[n])
		return num_atoms

def get_number_of_each_atom():
	with open('CONTCAR', 'r') as cont:
		for i in range(6): tmp = cont.readline()
		return cont.readline().split()

def get_sort_of_atoms():
	with open('CONTCAR', 'r') as cont:
		for i in range(5): tmp = cont.readline()
		return cont.readline().split()

###OUTCAR
def get_keyword_outcar(keyword):
	with open('OUTCAR', 'r') as out:
		for line in out:
			if keyword in line:
				return line.split()[2]

###DOSCAR
def split_DOSCAR(number_of_each_atom, sort_of_atoms, ISPIN, FORBITAL):
	##Fermi-level
	#FERMI = float(vasp.get_keyword_outcar('E-fermi'))
	##Skipping unnecessary part in DOSCAR
	doscar = open('DOSCAR')
	for i in range(5): tmp=doscar.readline()
	num_line = int(doscar.readline().split()[2])
	doscar.close

	doscar = open("DOSCAR", "r")
	for i in range(6): tmp = doscar.readline()

	#TDOS, considering ISPIN
	tdos = open("tDOS", "w")
	for i in range(num_line): tdos.write(doscar.readline().strip() + "\n")
	doscar.readline()

	#PDOS, considering either ISPIN and FORBITAL
	for n in range(len(number_of_each_atom)):
		atom = sort_of_atoms[n]
		print "found atom is " + atom
		for i in range(int(number_of_each_atom[n])):
			file_name = "pDOS_" + atom + "_" + str(i + 1)
			pdos = open(file_name, "w")
			for k in range(num_line): pdos.write(doscar.readline().strip() + "\n")
			doscar.readline()
	################################################
	############# writing itx for Igor #############
	################################################
	#tDOS.itx
	tdos_src = open("tDOS", "r")
	tdos_itx = open("tDOS.itx", "w")
	tdos_lines = tdos_src.readlines()
	tdos_itx.write("IGOR\n")
	if ISPIN == True:
		tdos_itx.write("WAVES/D " + "E_tdos_" + path + " TDOS_up_" + path + " TDOS_dw_" + path + " accum_up_" + path + " accum_dw_" + path)	
	else:
		tdos_itx.write("WAVES/D " + "E_tdos_" + path + " TDOS_" + path + " accum_" + path)		
	tdos_itx.write("\nBEGIN\n")
	for line in tdos_lines: tdos_itx.write(line)
	tdos_itx.write("END\n")
	if ISPIN == True:
		tdos_itx.write("X Display " + "TDOS_up_" + path + " vs " + "E_tdos_" + path + " as " + '"' + path + '"' + "\n")
	else:
		tdos_itx.write("X Display " + "TDOS_" + path + " vs " + "E_tdos_" + path + " as " + '"' + path + '"' + "\n")
	tdos_itx.write("""X ModifyGraph width=340.157,height=340.157
X ModifyGraph marker=19
X ModifyGraph lSize=1.5
X ModifyGraph tick=2
X ModifyGraph mirror=1
X ModifyGraph zero(bottom)=8
X ModifyGraph fSize=20
X ModifyGraph lblMargin(left)=15,lblMargin(bottom)=10
X ModifyGraph standoff=0
X ModifyGraph axThick=1.5
X ModifyGraph axisOnTop=1
X Label left "\\Z20 Density-of-states (arb. unit)"
X Label bottom "\\Z20 Energy (eV)"
"""
)

def sum_DOSCAR(atom, range_min, range_max):
	##make list of pdos file names
	file_list = []
	for a in range(range_min, range_max + 1):
		file_list.append("pDOS_" + atom + "_" + str(a))

	##make empty list for new list, named sum_dos
	pdos_first = [i.strip().split() for i in open("pDOS_" + atom + "_" + str(range_min)).readlines()]
	sum_dos = deepcopy(pdos_first)
	
	for i in range(len(sum_dos)):
		for k in range(len(sum_dos[0])):
			sum_dos[i][k] = 0

	##process of making summation of lists		
	print "Sum of ..."
	for file_name in file_list:
		print file_name + " ", 
		pdos = [i.strip().split() for i in open(file_name).readlines()]
	##convert all numbers from string to float
		for a in range(len(pdos)):
			for b in range(len(pdos[a])):
				pdos[a][b] = float(pdos[a][b])
	##sum of each element in all lists
		for n, line in enumerate(pdos):
			sum_dos[n] = map(sum, zip(line, sum_dos[n]))
	##correction energy values
	for i in range(len(pdos_first)):
		sum_dos[i][0] = pdos_first[i][0]

	##Output
	with open("sum_dos_" + atom + str(range_min) +"to" + str(range_max), "w") as output:
		output.writelines(' '.join(str(j) for j in i ) + "\n" for i in sum_dos)
	
	################################################
	############# writing itx for Igor #############
	################################################
	
