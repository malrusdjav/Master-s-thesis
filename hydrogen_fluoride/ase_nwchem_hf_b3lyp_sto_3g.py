from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
import ase.io
from ase.visualize import view
from ase.io import write

d = 1.0
hf = Atoms('HF',
           positions=[[0, 0, 0],
                      [0, 0, d]])

hf.calc = NWChem(dft=dict(iterations=500,xc='b3lyp'), basis='sto-3g')
#opt = BFGS(hf)
#opt.run(fmax=0.02)

for i in range(len(hf)): #distances for each atom in the molecule
        print(f"charge {i} : {hf.get_charges()[i]}")

print(hf.get_positions())

