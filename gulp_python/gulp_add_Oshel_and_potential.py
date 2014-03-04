#!/usr/bin/python

###Concatenate between gulp input file and source file containing the potential information
###Written by Su-Hyun Yoo
###Last update: 4 March 2014
###Needed input: gin file and "src" file with potential

input_name = "gulp_input.gin"
output_name = "gulp_output.gin"
a = open(input_name, "r")
b = open(output_name, "w")
c = open("/Users/suhyun/util_comp_sci/gulp_python/src", "r")

lines = a.readlines()
for n, line in enumerate(lines):
	if n == 0:
		new_line = "efg pot bond opti conp property compare phonon"
		b.write(new_line)
	elif n == 4:
		new_line = "title" + "\n"
		b.write(new_line)
	elif n == 5:
		new_line = input_name + "\n"
		b.write(new_line)
	elif n == 6:
		new_line = "end" + "\n"
		b.write(new_line)
	else:
		if line[0] == "p":
			break
		b.write(line)
		if line[0] == "O":
			list_line = list(line)
			list_line[5] = "s"
			list_line[6] = "h"
			list_line[7] = "e"
			list_line[8] = "l"
			str_line = ''.join(list_line)
			b.write(str_line)
	
lines_c = c.readlines()
for line in lines_c:
	b.write(line)
a.close()
b.close()
c.close()
