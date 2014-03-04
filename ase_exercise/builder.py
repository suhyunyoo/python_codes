#!/usr/bin/env python

from ase.lattice.spacegroup import crystal

def wurtzite(species, cell_par=[2,2,6,90,90,120],repititions=[1,1,1]):
         system = crystal((species),
         basis=[(2./3.,1./3.,0),(2./3.,1./3.,5./8.)],
         spacegroup=186, size = repititions, cellpar=cell_par)

         return system

def cubic_perovskite(species,cell_par=[6,6,6,90,90,90],repititions=[1,1,1]):
	 system = crystal((species), 
	 basis=[(0,0,0), (0.5, 0.5, 0.5), (0.5, 0.5, 0)],
         spacegroup=221, size = repititions, cellpar=cell_par)
	
         return system
