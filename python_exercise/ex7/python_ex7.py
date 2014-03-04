#!/usr/bin/env python
import glob
import os
import time

##Measure elapsed time
start_cpu = time.clock()
start_real = time.time()

print "######################################################################"
print "Python practice #7 26 November 2013"
print "Written by Daniel Yoo"
print ""


##Find current working directory
str1 = os.getcwd()
str2 = str1.split('/')
length_str2 = len(str2)
path = str2[length_str2 - 1]
print "Current path : " + path


##Find fermi energy and prep DOS source
outmol = open("outmol", "r")
Ef_report = open("Ef_" + path, "w")
lines = outmol.readlines()
for line in lines:
	if "Fermi" in line:
		Ef = line.split()
		Ef = Ef[4]
		EfeV = float(Ef) * 27.211396132
		Efigor = "%5.2f" % EfeV
		Ef_report.write("{} {} {}".format(str1, "Fermi level (eV)", EfeV))
		print "Fermi level in eV :",
		print Efigor
		print "Set Ef to zero."

outmol.close()
Ef_report.close()

##Total DOS title
TDOS_report = open("tDOS_" + path, "w")
TDOS_report.write('{} {}\n'.format("E_" + path, "TD_" + path))
TDOS_report.close()

##Total DOS title in PDOS data
DOS_report = open("DOS_" + path, "w")
lines=[]
lines.append('{} {} '.format("E_" + path, "TD_" + path))
DOS_report.writelines(lines)
DOS_report.close()


####Make TDOS source file

Natom = 0
outmol = open("outmol", "r")
TDOS_report = open("tDOS", "w")
atom_list = open("atom_list", "w")
outmol_lines = outmol.readlines()

for i, line in enumerate(outmol_lines):
	if "DOS" in line:
		for l in range(i + 1,i + 502):
			tdos_energy = float(outmol_lines[l].split()[0]) * 27.211396132 - EfeV
			tdos_dos = outmol_lines[l].split()[1]
			tdos_data = []
			tdos_data.append('{} {} \n'.format(tdos_energy, tdos_dos))
			TDOS_report.writelines(tdos_data)
	elif "Atom" in line:
		atom_info = []
		atom_info.append('{}'.format(line))
		atom_list.writelines(atom_info)
		Natom += 1

outmol.close()
TDOS_report.close()
atom_list.close()


##Make PDOS_title & data files
print ""
print "Pick atoms to be selected"
atom_list = open("atom_list","r")
outmol = open("outmol","r")
DOS_report = open("DOS_" + path, "w")
lines_atom_list = atom_list.readlines()
lines_outmol = outmol.readlines()

for i in range(0,Natom):
	
	Atomname = lines_atom_list[i].split()[2]
	Atomnum = lines_atom_list[i].split()[1]
	pDOS_source = open("pDOS_" + Atomname + "_" + Atomnum,"w")
	DOS_report.write('{} {} {}'.format(path+"_"+Atomname+"_"+Atomnum+"_"+"s", path+"_"+Atomname+"_"+Atomnum+"_"+"p", path+"_"+Atomname+"_"+Atomnum+"_"+"d"))

	for n, line in enumerate(lines_outmol):
		if Atomnum + "  " + Atomname in line:
			print Atomnum + "  " + Atomname
			for l in range(n + 1,n + 502):
				lines_s = lines_outmol[l].split()[0]
				lines_p = lines_outmol[l].split()[0]
				lines_d = lines_outmol[l].split()[0]
				pDOS_source.write('{} {} {} \n'.format(lines_s, lines_p, lines_d))

	pDOS_source.close()

atom_list.close()
outmol.close()
DOS_report.close()


##Collect pdos data

#atom_list = open("atom_list","r")
#outmol = open("outmol","r")
#DOS_report = open("DOS_" + path, "w")
#lines_atom_list = atom_list.readlines()
#lines_outmol = outmol.readlines()

#for i in range(0,Natom):
#	
#	Atomname = lines_atom_list[i].split()[2]
#	Atomnum = lines_atom_list[i].split()[1]
#
#	vars()["lines_" + Atomname + Atomnum] = 
#	aaaa=[]
#	for i, e in enumerate(vars()["lines_" + Atomname + Atomnum]):
#		vars()["lines_" + Atomname + Atomnum][i] = vars()["lines_" + Atomname + Atomnum][i].replace('\n',' ')
#		aaaa = vars()["lines_"+Atomname+Atomnum][i]
#		print aaaa

print "Number of atoms :", Natom

##make igor style file
#a = open("TDOS_"+path+".ipf", "w")
#a.write("""#pragma rtGlobals=1
#	Window ig_$path() : Graph
#        PauseUpdate; Silent 1           // building window...
#        Display /W=(451,398,1025,822) TD_$path vs E_$path
#        ModifyGraph width=453.543,height=340.157
#        ModifyGraph lSize=1.5
#        ModifyGraph rgb=(0,0,0)
#        ModifyGraph tick=2
#        ModifyGraph zero(bottom)=9
#        ModifyGraph mirror=1
#        ModifyGraph font="Times New Roman"
#        ModifyGraph fSize=20
#        ModifyGraph lblMargin(left)=9
#        ModifyGraph standoff=0
#        ModifyGraph lblLatPos(left)=-4
#        ModifyGraph manTick(left)={0,200,0,0},manMinor(left)={1,50}
#        Label left "\\Z20Density-of-states (arb.)"
#        Label bottom "\\Z20Energy, E-E\\BF\\M\\Z20 (eV)"
#        SetAxis bottom -6,6
#        TextBox/C/N=text1/F=0/A=MC/X=-19.82/Y=41.18 "\\F'Times New Roman'\\Z18TD_$path"
#        Legend/C/N=text0/J/F=0/B=1/A=MC/X=30.18/Y=34.41 "\\F'Times New Roman'\\Z20\r\\s(TD_$path) TDOS\rE\\BF\\M\\Z20 = $Efigor eV"
#EndMacro
#""")
#a.close()



#filelist = glob.glob("pDOS*")
#for f in filelist:
#	os.remove(f)
#os.remove("TDOS")
#os.remove("atom_list")




##Measure elapsed time #2
end_cpu=time.clock()
end_real=time.time()
print ""
print "Elapsed time"
print("%f Real Seconds" % (end_real - start_real))
print("%f Cpu Seconds" % (end_cpu - start_cpu))

print "######################################################################"