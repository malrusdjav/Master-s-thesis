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

eps = 0.35
r_min = eps
r_max = 2.0
n = 10 
dr = (r_max - r_min)/n
r_curr = r_min

E_H, E_F = 0, 0 # the energies of individual atoms (physical constants)
E = [] # bound HF molecular energy (contains a list of such energies for different xc functionals)
curr_energy_spectrum = []
dE = [] # energy difference (contains a list of such differences for different xc functionals)
d = [] # distance 
exc_corr = ['b3lyp', 'pbe0'] # exchange correlation functionals (xc)
bs = ['sto-2g', 'sto-3g', 'sto-6g'] # basis sets (bs)

xc = dict() # keys: xc, values: bs => within each bs there're two lists: 
	           			#1 bound energy (list of such energies for different bs)
					#2 energy difference (list of such differences for different bs)
for i in range(len(exc_corr)):
	xc[f'{exc_corr[i]}'] = dict()
	for j in range(len(bs)):
		xc[f'{exc_corr[i]}'][f'{bs[j]}'] = []
		
print(xc)

for i in range(n):
	d.append(r_curr)
	r_curr+=dr

for i in range(len(exc_corr)):
	for j in range(len(bs)):
		for k in range(n):
			hf = Atoms('HF', positions=[[0, 0, 0], [0, 0, d[k]]])
			hf.calc = NWChem(dft=dict(iterations=500,xc=exc_corr[i]), basis=bs[j])	
			curr_energy_spectrum.append(hf.get_potential_energy())
			#curr_energy_spectrum.append(k)
		xc[f'{exc_corr[i]}'][f'{bs[j]}'].append(curr_energy_spectrum)	
		curr_energy_spectrum = []
	
#print(E)
print('\n\n')


curr_dE = []
for i in range(len(exc_corr)):
        for j in range(len(bs)):
                print(f'E_H and E_F for xc: {exc_corr[i]}, bs: {bs[j]}')
		
                h = Atoms('H', positions=[[0, 0, 0]])
                h.calc = NWChem(dft=dict(iterations=500,xc=exc_corr[i],mult=2), basis=bs[j])
                E_H = h.get_potential_energy()        

                f = Atoms('F', positions=[[0, 0, 0]])
                f.calc = NWChem(dft=dict(iterations=500,xc=exc_corr[i], mult=2), basis=bs[j])
                E_F = f.get_potential_energy()

                for k in range(n):
                        hf = Atoms('HF', positions=[[0, 0, 0], [0, 0, d[k]]])
                        hf.calc = NWChem(dft=dict(iterations=500,xc=exc_corr[i]), basis=bs[j])
                        curr_dE.append(xc[f'{exc_corr[i]}'][f'{bs[j]}'][0][k] - (E_H + E_F))
                       	#curr_energy_spectrum.append(k)
                xc[f'{exc_corr[i]}'][f'{bs[j]}'].append(curr_dE)
                curr_dE = []


		#curr_dE.append(j - (E_H + E_F))
	#dE.append(curr_dE)
	#xc[f'{exc_corr[i]}'][f'{bs[j]}'][1].append(curr_dE)
	#xc[f'{exc_corr[i]}'][f'{bs[j]}'].append([1, 2, 3])
	#curr_dE = []
print(xc)
#for i in range(len(exc_corr)):

'''
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Potential curves for the HF molecule')
ax1.plot(d, xc[f'{exc_corr[0]}'][f'{bs[0]}'][1], d, xc[f'{exc_corr[0]}'][f'{bs[1]}'][1], d,  xc[f'{exc_corr[0]}'][f'{bs[2]}'][1], '-o')
ax1.set_xlabel('Distance')
ax1.set_ylabel('Energy')
#ax.set_title('Potential curves for the HF molecule')
ax1.legend([f'{exc_corr[0], bs[0]}', f'{exc_corr[0], bs[1]}', f'{exc_corr[0], bs[2]}'], fontsize = "5", loc="upper right")

ax2.plot(d, xc[f'{exc_corr[1]}'][f'{bs[0]}'][1], d, xc[f'{exc_corr[1]}'][f'{bs[1]}'][1], d,  xc[f'{exc_corr[1]}'][f'{bs[2]}'][1], '-o')
ax2.set_xlabel('Distance')
ax2.set_ylabel('Energy')
#ax.set_title('Potential curve for the HF molecule')
ax2.legend([f'{exc_corr[1], bs[0]}', f'{exc_corr[1], bs[1]}', f'{exc_corr[1], bs[2]}'], fontsize = "5", loc="upper right")

fig.tight_layout(pad=3.0)
plt.show()
'''


fig, ax = plt.subplots()
ax.plot(d, xc[f'{exc_corr[0]}'][f'{bs[0]}'][1], d, xc[f'{exc_corr[0]}'][f'{bs[1]}'][1], d,  xc[f'{exc_corr[0]}'][f'{bs[2]}'][1], '-o')
ax.set_xlabel('Distance')
ax.set_ylabel('Energy')
ax.set_title(f'Potential curves for the HF molecule, {exc_corr[1]}')
plt.legend([f'{exc_corr[0], bs[0]}', f'{exc_corr[0], bs[1]}', f'{exc_corr[0], bs[2]}'], loc="upper right")
plt.show()


fig, ax = plt.subplots()
ax.plot(d, xc[f'{exc_corr[1]}'][f'{bs[0]}'][1], d, xc[f'{exc_corr[1]}'][f'{bs[1]}'][1], d,  xc[f'{exc_corr[1]}'][f'{bs[2]}'][1], '-o')
ax.set_xlabel('Distance')
ax.set_ylabel('Energy')
ax.set_title(f'Potential curves for the HF molecule, {exc_corr[1]}')
plt.legend([f'{exc_corr[1], bs[0]}', f'{exc_corr[1], bs[1]}', f'{exc_corr[1], bs[2]}'], loc="upper right")
plt.show()





