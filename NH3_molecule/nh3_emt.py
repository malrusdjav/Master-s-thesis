from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton

system = Atoms('NH3', positions=[[0.0, 0.0, 0.0],
                                    [0.0, 0.0, 1.0], [0.0, 0.0, 2.0], [0.0, 0.0, 3.0]])
calc = EMT()#effective medium theory

system.calc = calc #calculator
opt = QuasiNewton(system, trajectory='nh3.emt.traj')
opt.run(fmax=0.02)
