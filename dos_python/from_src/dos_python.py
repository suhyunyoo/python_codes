#!/usr/bin/env python
import matplotlib.pyplot as plt
import math
from os import getcwd
from time import clock, time

##Measure elapsed time
start_cpu = clock()
start_real = time()

##Find current working directory
path = getcwd().split('/')[-1]
print "Current path : " + path

##make each array for x and y axis from src file
x1 = []
y1 = []
src = open('src', 'r')
lines = src.readlines()
for n, line in enumerate(lines):
	list_line = line.split(" ")
	if n == 0:
		name_list = [word.strip() for word in list_line]
		x_name = name_list[0]
		y_name = name_list[1] 
	else:
		x1.append(list_line[0])
		y1.append(list_line[1])

##plot using matplotlib
print "1. Plot DOS using matplotlib,",
fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.set_xlim(float(x1[0]),float(x1[-1]))
plt.xlabel(x_name)
plt.ylabel(y_name)
plt.show()
print "======> done"

##make itx file for igor
print "2. Writing itx file for igor,",
itx_name = path + ".itx"
b = zip(x1, y1)
itx = open(itx_name, "w")
itx.write("IGOR\n")
itx.write("WAVES/D " + x_name + " " + y_name)
itx.write("\nBEGIN\n")
for i in b:
	itx.write("{} {}\n".format(i[0],i[1]))
itx.write("END\n")
itx.write("X Display " + y_name + " vs " + x_name + " as " + '"' + path + '"' + "\n")
itx.write("""X ModifyGraph width=340.157,height=340.157
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
"""X SetAxis bottom """ + str(math.floor(float(x1[0]))) + "," + str(math.floor(float(x1[-1]))) + """
""" + """X TextBox/C/N=text0/F=0/B=1/A=MC/X=30.29/Y=37.06 "\\Z20\\s(""" + y_name + """)""" + y_name + '"'
)
print "======> done"
####Other options
#X TextBox/C/N=text1/D=1.5/B=(65535,65534,49151)/A=LT/X=-0.78/Y=-0.29 "\\Z24K/Pd"
#X ModifyGraph manTick(left)={0,0.03,0,2},manMinor(left)={0,50}
#X ModifyGraph manTick(bottom)={0,0.5,0,1},manMinor(bottom)={0,50}
#X Label left "\\F'symbol'g\\F'times new roman' (eV/\\{num2char(129)}\\S2\\M\\Z24)"
#X Label bottom "\\F'symbol'D\\f02m\\f00\\F'Times new roman'\\BK\\M\\Z24 (eV)"
#X SetAxis left 0,0.15


##Measure elapsed time #2
end_cpu=clock()
end_real=time()
print ""
print "Elapsed time"
print("%.2f Real Seconds" % (end_real - start_real))
print("%.2f Cpu Seconds" % (end_cpu - start_cpu))

