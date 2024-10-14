from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
from ase.io import write

nh3 = Atoms('NH3',positions=[[0, 0, 0],[0, 2.4, 2.1],[0, -1.4, 5.1],[0, 3.4, -2.1]])
nh3.calc = NWChem(xc='PBE')
opt = BFGS(nh3, trajectory='nh3.traj')
opt.run(fmax=0.02)


