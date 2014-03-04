#!/usr/bin/python

###transforming cif to vasp format, using ASE.
###Written by Su-Hyun Yoo
###Last update: 4 March 2014
###Needed input: cif file
###Used library: sys, ase, ase.io, ase.io.vasp, ase.io.cif

import ase
import ase.io
from ase.io import vasp
from ase.io import cif
import sys

file_name = sys.argv[1]
print str(file_name)

test = ase.io.cif.read_cif(file_name)
ase.io.vasp.write_vasp(file_name + ".vasp",test,sort='True',direct='True',vasp5='True')
print "Done"