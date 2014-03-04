#!/usr/bin/env python

import ase
import builder
from ase.io import vasp

#making poscar
zno = builder.wurtzite(['Zn','O'],cell_par=[3.2376825,3.2376825,5.2282598,90,90,120],repititions=[1,1,1])
ase.io.vasp.write_vasp('ZnO_POSCAR',zno,sort='True',direct='True')

#postprocess poscar
a = open("ZnO_POSCAR","r")
lines = a.readlines()
lines.insert(5,lines[0])
a = open("ZnO_POSCAR","w")

for b in lines:
        a.write(b)
a.close()
