from ase import Atoms
import ase.db
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
h = Atoms('H2')
h.calc = EMT()
h.get_potential_energy()

row = db.get(relaxed=1, calculator='emt')
e2 = row.energy
e1 = db.get(H=1).energy
ae = 2 * e1 - e2
print(ae)
