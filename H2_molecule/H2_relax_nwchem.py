#Example: structure optimization of hydrogen molecule
from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
from ase.io import write
d = 1.0
h2 = Atoms('H2',
           positions=[[0, 0, 0],
                      [0, 0, d]])
h2.calc = NWChem(xc='PBE')
opt = BFGS(h2)
opt.run(fmax=0.02)
