from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
import ase.io
from ase.visualize import view
from ase.io import write
import numpy as np
import matplotlib.pyplot as plt

'''Here I am trying to add different
basis sets + and functionals and then
I am going to visualize the data on the same
plot '''

eps = 0.5
r_min = eps
r_max = 2.0
n = 10 
dr = (r_max - r_min)/n
r_curr = r_min

E_H, E_F = 0.2, 1 # the energies of individual atoms (physical constants)
E = [] # bound HF molecular energy (contains a list of such energies for different xc functionals)
curr_energy_spectrum = []
dE = [] # energy difference (contains a list of such differences for different xc functionals)
d = [] # distance 
exc_corr = ['b3lyp', 'pbe0'] # exchange correlation functionals
bs = ['sto-2g', 'sto-3g'] # basis sets

b3lyp = dict()
pbe0 = dict()
hse03 = dict()

for i in range(n):
	d.append(r_curr)
	r_curr+=dr

for i in range(len(exc_corr)):
	for j in range(n):
		hf = Atoms('HF', positions=[[0, 0, 0], [0, 0, d[j]]])
		hf.calc = NWChem(dft=dict(iterations=500,xc=exc_corr[i]), basis='sto-3g')	
		curr_energy_spectrum.append(hf.get_potential_energy())
	E.append(curr_energy_spectrum)
	curr_energy_spectrum = []
	
#print(E)
print('\n\n')

curr_dE = []
for i in range(len(E)):
	for j in E[i]:
		curr_dE.append(j - (E_H + E_F))
	dE.append(curr_dE)
	curr_dE = []
#print(dE[0])
#print(d)

fig, ax = plt.subplots()
ax.plot(d, dE[0], d, dE[1], '-o')
ax.set_xlabel('Distance')
ax.set_ylabel('Energy')
ax.set_title('Potential curve for the HF molecule')
#plt.plot(d, dE[0], "-b", label='b3lyp')
#plt.plot(d, dE[1], "-r", label='pbe0')
#plt.legend(loc="upper left")
#plt.ylim(-1.5, 2.0)
plt.legend([f'{exc_corr[0]}', f'{exc_corr[1]}'], loc="upper right")
plt.show()

