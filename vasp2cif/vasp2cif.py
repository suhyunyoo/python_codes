#!/usr/bin/python

###transforming vasp to cif format, using ASE.
###Written by Su-Hyun Yoo
###Last update: 4 March 2014
###Needed input: vasp file
###Used library: sys, ase, ase.io, ase.io.vasp, ase.io.cif

import ase
import ase.io
from ase.io import vasp
from ase.io import cif
import sys

file_name = sys.argv[1]
print str(file_name)

sample = ase.io.vasp.read_vasp(file_name)
ase.io.cif.write_cif(file_name + ".cif",sample)
print "Done"