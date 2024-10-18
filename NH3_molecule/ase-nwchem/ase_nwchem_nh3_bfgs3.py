from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
import ase.io
from ase.visualize import view
from ase.io import write
#from pathlib import Path

nh3coor = ase.io.read(filename='./avogadro/nh3_uff.xyz', format='xyz',index=":")
#view(nh3coor)
print(nh3coor)
print(nh3coor[0])
print(nh3coor[0].symbols)
print("initial NH3 positions : \n ", nh3coor[0].positions)

#print(nh3coor[0].positions)


#nh3 = Atoms('NH3',positions=[[0, 0, 0],[0, 2.4, 2.1],[0, -1.4, 5.1],[0, 3.4, -2.1]])
nh3 = Atoms('NH3',positions=nh3coor[0].positions)

nh3.calc = NWChem(dft=dict(iterations=500,xc='B3LYP'))
opt = BFGS(nh3, trajectory='nh3.traj')
opt.run(fmax=0.02)

print('NH3 positions:')
print(nh3.positions)

print('file with final coordinates written ... nh3_new.xyz')
ase.io.write(filename="nh3_new.xyz", images=nh3, format="xyz")

#for i in range(len(nh3)):
#    for j in range(len(nh3)):
#	for k in range(len(nh3)):
#	    print(nh3.get_angle(i,j,k))
# nested list comprehensions
#angles = [[[print(nh3.get_angle(i,j,k))] for i in range(len(nh3)) for j in range(len(nh3))] for k in range(len(nh3))]
print(nh3)

for i in range(len(nh3)):
	print(f'position {i}: atom {nh3.symbols:}') 
print("Distance: ", nh3.get_distance(0, 1))       
print(f"Numbers of atoms  : {len(nh3)}") #number of atoms in the molecule
print("Angles: ", nh3.get_angle(0, 1, 2), nh3.get_angle(1,2,3), nh3.get_angle(1,2,3)) #all unique angles
print(f"massess  : {nh3.get_masses()}") #distances (displayed as an array)
for i in range(len(nh3)): #distances for each atom in the molecule
	print(f"mass {i} : {nh3.get_masses()[i]}")
write('NH3_nwchem.xyz', nh3)
