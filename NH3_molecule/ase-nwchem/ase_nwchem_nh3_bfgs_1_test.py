from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
import ase.io
from ase.visualize import view
from ase.io import write
from tabulate import tabulate
import statistics

nh3coor = ase.io.read(filename='./avogadro/nh3_uff.xyz', format='xyz',index=":")
#nh3coor = ase.io.read('nh3_uff.xyz', format='xyz',index=":")
#view(nh3coor)
print(nh3coor)
print(nh3coor[0])
print(nh3coor[0].symbols)
print("initial NH3 positions : \n ", nh3coor[0].positions)

#print(nh3coor[0].positions)


#nh3 = Atoms('NH3',positions=[[0, 0, 0],[0, 2.4, 2.1],[0, -1.4, 5.1],[0, 3.4, -2.1]])
nh3 = Atoms('NH3',positions=nh3coor[0].positions)

exc_corr = ['b3lyp', 'pbe0', 'hse03'] # exchange correlation functionals
#exc_corr = ['b3lyp']

#file = open('res.txt', 'w')

data = []
dist_av = [] #average distance
ang1_av = []
ang2_av = []
ang3_av = []
#angles: list[list[float]] = []

#for i in range(len(exc_corr)):
#	print(f'\nRunning exchange correlation: {exc_corr[i].upper()}')
#	nh3.calc = NWChem(dft=dict(iterations=500,xc=exc_corr[i]))
#	opt = BFGS(nh3, trajectory='nh3.traj')
#	opt.run(fmax=0.02)
#	#file.write(f'Angles: {nh3.get_angle(0, 1, 2)} {nh3.get_angle(1,2,3)} {nh3.get_angle(1,2,3)})
#	
#	ang_3 = [nh3.get_angle(0, 1, 2), nh3.get_angle(1, 2, 3), nh3.get_angle(2, 1, 3)]
#	angles_int = [round(ang, 5) for ang in ang_3] 	
#	#angles ='\n'.join(map(str, [nh3.get_angle(0, 1, 2), nh3.get_angle(1, 2, 3), nh3.get_angle(2, 1, 3)]))
#	angles ='\n'.join(map(str, angles_int))
#
#	data.append([exc_corr[i], nh3.get_distance(0, 1), angles])
#	ang1_av.append(nh3.get_angle(0, 1, 2))
#	ang2_av.append(nh3.get_angle(1, 2, 3))
#	ang3_av.append(nh3.get_angle(2, 1, 3))
#	#dist.append(nh3.get_distance(0, 1))	

#	print("Distances: ", nh3.get_distance(0, 1))
#	print(f'Computation with XC: {exc_corr[i].upper()} is successfully completed!\n')

#for i in range(len(data)):
#	dist_av.append(data[i][1])
#av = statistics.mean(dist_av)
#a1_av = statistics.mean(ang1_av)
#a2_av = statistics.mean(ang2_av)
#a3_av = statistics.mean(ang3_av)

#av_ang123 = '\n'.join(map(str, [a1_av, a2_av, a3_av]))
#data.append(['average', av, av_ang123])
#data.append(['experiment', 1.0124, ])
#file.write(tabulate(data, headers=["XC functional", "Distance", "Angles"]))

#file.close()
print('\n\n')

print('NH3 positions:')
print(nh3.positions)

print('file with final coordinates written ... nh3_new.xyz')
ase.io.write(filename="nh3_new.xyz", images=nh3, format="xyz")

print(nh3)

for i in range(len(nh3)):
	print(f'position {i}: atom {nh3.symbols[i]}') 
print("Distance: ", nh3.get_distance(0, 1))       
print(f"Numbers of atoms  : {len(nh3)}") #number of atoms in the molecule
print(f' HHH {nh3.get_angle(1, 2, 3)}  HNH {nh3.get_angle(2, 0, 1)}  NH {nh3.get_angle(0, 1, 2)} ') #all unique angles
print(f"massess  : {nh3.get_masses()}") #distances (displayed as an array)
for i in range(len(nh3)): #distances for each atom in the molecule
	print(f"mass {i} : {nh3.get_masses()[i]}")

#print(f'The average distance equals {statistics.mean(dist)}')
write('NH3_nwchem.xyz', nh3)
