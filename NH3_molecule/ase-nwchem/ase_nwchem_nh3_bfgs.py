from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
import ase.io
from ase.visualize import view
#from pathlib import Path

nh3coor = ase.io.read('./avogadro/nh3_uff.xyz', format='xyz',index=":")
#view(nh3coor)
print(nh3coor)
print(nh3coor[0])
print(nh3coor[0].symbols)

#print(nh3coor[0].positions)


#nh3 = Atoms('NH3',positions=[[0, 0, 0],[0, 2.4, 2.1],[0, -1.4, 5.1],[0, 3.4, -2.1]])
nh3 = Atoms('NH3',positions=nh3coor[0].positions)

nh3.calc = NWChem(dft=dict(iterations=500,xc='B3LYP'))
opt = BFGS(nh3, trajectory='nh3.traj')
opt.run(fmax=0.02)

print('Optimized NH3 positions:')
print(nh3coor[0].positions)

