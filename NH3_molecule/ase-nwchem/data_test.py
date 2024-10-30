from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
import ase.io
from ase.visualize import view
from ase.io import write

xc=['b3lyp','pbe0']
bs=['sto-3g','cc-pVDZ']

data[xc[0],bs[0]]=
