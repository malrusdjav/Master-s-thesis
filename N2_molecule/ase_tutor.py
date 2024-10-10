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

a = 5.387
crystal = Atoms('Zn4S4',
                scaled_positions=[[0., 0., 0.],
                           [0., 0.5, 0.5],
                           [0.5, 0., 0.5],
                           [0.5, 0.5, 0.],
                           [0.25, 0.75, 0.75],
                           [0.25, 0.25, 0.25],
                           [0.75, 0.75, 0.25],
                           [0.75, 0.25, 0.75]],
               cell=[a, a, a],
               pbc=True)
#view(moleculeN2)
