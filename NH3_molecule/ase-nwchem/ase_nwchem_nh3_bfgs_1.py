from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.nwchem import NWChem
import ase.io
from ase.visualize import view
from ase.io import write
from tabulate import tabulate
import statistics
from pytablewriter import UnicodeTableWriter

nh3coor = ase.io.read(filename='./avogadro/nh3_uff.xyz', format='xyz',index=":")
#nh3coor = ase.io.read('nh3_uff.xyz', format='xyz',index=":")
#view(nh3coor)
print(nh3coor)
print(nh3coor[0])
print(nh3coor[0].symbols)


f_opt = open('opt.txt', 'w')
f_opt.write("initial NH3 positions : " + '\n')
f_opt.write(str(nh3coor[0].positions) + '\n\n\n')
#print("initial NH3 positions : \n ", nh3coor[0].positions)

nh3 = Atoms('NH3',positions=nh3coor[0].positions)

bs = ['sto-2g', 'sto-3g', 'sto-6g']
#bs = ['sto-2g', 'sto-3g']
exc_corr = ['b3lyp', 'pbe0', 'hse03'] # exchange correlation functionals
#exc_corr = ['b3lyp', 'pbe0']

file = open('res.txt', 'w')

data = []
exp_data = ['experiment', None, round(1.0124, 4), None, round(106.670, 3)]

ang_var = [] #average angle (within one functional)
ang3_av = []

dist_av = [] #average distance (within one functional)
dist_var = []

errors = dict() #all re's and their pairs of XS + BS

for i in range(len(exc_corr)):
	for j in range(len(bs)):
		print(f'\nRunning exchange correlation: {exc_corr[i].upper()}')
		nh3.calc = NWChem(dft=dict(iterations=500,xc=exc_corr[i]), basis=bs[j])
		opt = BFGS(nh3, trajectory='nh3.traj')
		opt.run(fmax=0.02)
		
		ang_3 = [nh3.get_angle(1, 0, 3), nh3.get_angle(1, 0, 2), nh3.get_angle(2, 0, 3)]	
		ang3_av = round(statistics.mean(ang_3), 3)
		ang_var = round(statistics.variance(ang_3), 9)		
 		
		#angles_int = [round(ang, 5) for ang in ang_3] 	
		#angles ='\n'.join(map(str, angles_int))

		dist_3 = [ nh3.get_distance(0, 1),  nh3.get_distance(0, 2),  nh3.get_distance(0, 3)]	
		dist_av = round(statistics.mean(dist_3), 4)		
		dist_var = round(statistics.variance(dist_3), 12)
		
		# relative error (combined)
		re = round(abs(((dist_av - exp_data[2])/exp_data[2] + (ang3_av - exp_data[4])/exp_data[4]))*100, 3)  
		errors[re] = [exc_corr[i], bs[j]]		

		data.append([exc_corr[i], bs[j], dist_av, dist_var, ang3_av, ang_var, re])	
		print(f'Computation with XC: {exc_corr[i].upper()} and BS: {bs[j]} is successfully completed!\n')

data.append(exp_data)

headers = ["XC", "BS", "Mean dist", "Dist var",
           "Mean angle", "Angle var", "RE"]

file.write(tabulate(data, headers))

min_error = min(errors)
min_set = ' + '.join(errors[min_error])
#file.write(f'\nThe minimum relative error is equal to {min_error}')
#file.write(f'\nIt is achieved with the following combination of XC and BS {min_set}\n')
print('\n\n')

f_opt.write('Optimized positions: ' + '\n')
f_opt.write(str(nh3.positions))

print('file with final coordinates written ... nh3_new.xyz')
ase.io.write(filename="nh3_new.xyz", images=nh3, format="xyz")

print(nh3)

for i in range(len(nh3)):
	print(f'position {i}: atom {nh3.symbols:}')

file.close()
f_opt.close()

def printer(data, headers):
    writer = UnicodeTableWriter(
        table_name="example_table",
        headers=headers,
	value_matrix=data
    )
    
    file = open('output.txt', 'w')
    file.write(writer.dumps())

    #file.write(f'\n\nThe minimum relative error is equal to {min_error}')
    #file.write(f'\nIt is achieved with the following combination of XC and BS {min_set}\n')
    file.close()

printer(data, headers)

print("Distance: ", nh3.get_distance(0, 1))       
print(f"Numbers of atoms  : {len(nh3)}") #number of atoms in the molecule
print(f"massess  : {nh3.get_masses()}") #distances (displayed as an array)
for i in range(len(nh3)): #distances for each atom in the molecule
	print(f"mass {i} : {nh3.get_masses()[i]}")

#print(f'The average distance equals {statistics.mean(dist)}')
write('NH3_nwchem.xyz', nh3)
