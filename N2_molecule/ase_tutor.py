from ase.visualize import view
from ase import Atoms
d = 1.10
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from ase.visualize import view
moleculeN2 = Atoms('N2', positions=[(0., 0., 0.), (0., 0., d)])
from ase.geometry import get_distances
calc = EMT()
moleculeN2.calc = calc #calculator

opt = QuasiNewton(moleculeN2, trajectory='n2.emt.traj')
opt.run(fmax=0.05)
# print optimizaed distace

print (moleculeN2.get_distance(0,1))


#view(moleculeN2)
