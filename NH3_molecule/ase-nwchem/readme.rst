====================
NH3 with ase-nwchem
====================

Calculation of data on the properties of the ammonia molecule:
1) average distance between N and H atoms  in the molecule
2) average angle between HNH atoms in the molecule
3) variance was calculated for 1) and 2)
4) Based on the calculations and experimental data, the minimum relative error in the calculations was calculated, 
which was used to determine the optimal combination of XC and BS



Calculations were performed for the following set of exchange correlation functionals (XC):
['b3lyp', 'pbe0', 'hse03']

Each functional has been tested in the following basis sets (BS):
['sto-2g', 'sto-3g', 'sto-6g'] 

According to the results of calculations, the most optimal pair of XC and BS turned out to be the following 
combination:
b3lyp + sto-3g



