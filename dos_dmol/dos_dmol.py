import os
import subprocess
import sh_common as common

##calculate elapsed time1
start_time = common.get_start_time()

##Find current working directory
path = os.getcwd().split('/')[-1]
print "Current path : " + os.getcwd() +"\n"

subprocess.call(["./dmol_dos_part.sh"])

################################################
############# writing itx for Igor #############
################################################
#DOS.itx
dos_src = open("DOS_" + path + ".dat", "r")
dos_itx = open("DOS_" + path + ".itx", "w")
dos_lines = dos_src.readlines()	
dos_itx.write("IGOR\n")

for i, line in enumerate(dos_lines):
	if i == 0:
		dos_itx.write("WAVES/D ")
		dos_itx.write(line)
		dos_itx.write("BEGIN\n")
	else:
		dos_itx.write(line)

dos_itx.write("END\n")
print dos_lines[0].split()[0]
print dos_lines[0].split()[1]
dos_itx.write("X Display " + str(dos_lines[0].split()[1]) + " vs " + str(dos_lines[0].split()[0]) + " as " + '"' + path + '"' + "\n")

dos_itx.write("""X ModifyGraph width=340.157,height=340.157
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
dos_src.close()
dos_itx.close()