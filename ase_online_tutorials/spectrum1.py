from ase import Atoms
from ase.lattice import FCC
from ase.units import Bohr

si_fcc = Atoms(symbols='Si2',
               cell = FCC(a=10.20*Bohr).tocell(),
               scaled_positions=[(0.0, 0.0, 0.0),
                                 (0.25, 0.25, 0.25)],
               pbc=True)


from pathlib import Path
import json

pseudo_dir = Path.home() / 'SSSP_1.2.1_PBE_efficiency'
with open(str(pseudo_dir / 'SSSP_1.2.1_PBE_efficiency.json')) as fj:
  dj = json.load(fj) 
ecutwfc = dj['Si']['cutoff_wfc']
ecutrho = dj['Si']['cutoff_rho']

atomic_species = {'Si':dj['Si']['filename']}
