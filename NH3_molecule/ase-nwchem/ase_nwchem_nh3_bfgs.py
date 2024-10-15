from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
from ase.io import write
from ase import io

nh3coor = io.read('./avogadro/nh3_uff.xyz', format='xyz',index=":")

#nh3 = Atoms('NH3',positions=[[0, 0, 0],[0, 2.4, 2.1],[0, -1.4, 5.1],[0, 3.4, -2.1]])
nh3 = Atoms('NH3',positions=nh3coor)

#nh3.calc = NWChem(dft=dict(iterations=500,xc='B3LYP'))
#opt = BFGS(nh3, trajectory='nh3.traj')
#opt.run(fmax=0.02)


