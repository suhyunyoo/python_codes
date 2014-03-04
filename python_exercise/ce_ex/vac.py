## Vacuum control program
## Built for VASP 4.6 or above format
## Built as a preliminary work as a part of MTG Materials Tool Kit.
## By Johnny Chang-Eun Kim,  April. 2013
from vacuum_agent import *
from sys import argv
##where='0.5'
##howmuch='-10.0'
target=load('POSCAR', 'vacuum_edit')
where=argv[1]
howmuch=argv[2]
target.add_vacuum(float(where), float(howmuch))
File=open('POSCAR_vac_edited', 'w'); File.write(target.buildPOSCAR()); File.close()
