from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
import ase.io
from ase.visualize import view
from ase.io import write
import ase.io.castep
import matplotlib.pyplot as plt

eps = 0.5
r_min = eps
r_max = 2.0
n = 10 
dr = (r_max - r_min)/n

r_curr = r_min

E_H, E_F = 0.2, 1 # the energies of individual atoms
E = [] # bound HF molecular energy
curr_energy_spectrum = []
dE = [] # energy difference 
dE2 = []
dist = []
xc = ['b3lyp', 'pbe0']
#for functional in xc:
for i in range(n):
	hf = Atoms('HF', positions=[[0, 0, 0], [0, 0, r_curr]])
	hf.calc = NWChem(dft=dict(iterations=500,xc='b3lyp'), basis='sto-3g')
	E.append(hf.get_potential_energy())
	dist.append(r_curr)
	r_curr+=dr

for i in range(n):
	dE.append(E[i] - (E_H + E_F))
print(dE)

fig, ax = plt.subplots()
ax.plot(dist, dE, '-o')
ax.set_xlabel('Distance')
ax.set_ylabel('Energy')
ax.set_title('Potential curve for the HF molecule')
plt.show()
