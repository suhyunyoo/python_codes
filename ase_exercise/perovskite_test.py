#!/usr/bin/env python

import ase
import builder
from ase.io import vasp

#making poscar
zno = builder.cubic_perovskite(['Ca','Ti','O'],cell_par=[3.813,3.813,3.813,90,90,90],repititions=[1,1,1])
ase.io.vasp.write_vasp('CaTiO3_POSCAR',zno,sort='True',direct='True')

#postprocess poscar
a = open("CaTiO3_POSCAR","r")
lines = a.readlines()
b = open("CaTiO3_POSCAR","w")

for a in range(0,5):
        b.write(lines[a])
b.write(lines[0])
for a in range(5,len(lines)):
        b.write(lines[a])

b.close()
