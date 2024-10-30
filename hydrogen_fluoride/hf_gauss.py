from ase.calculators.gaussian import Gaussian
from ase import Atoms

calc = Gaussian(label='calc/gaussian',
                xc='B3LYP',
                basis='6-31+G*',
                scf='maxcycle=100')

hf = Atoms('HF', [[0, 0, 0], [0, 0, 0.74]])
hf.calc = Gaussian(mem='1GB',
                      chk='MyJob.chk',
                      save=None,
                      method='b3lyp',
                      basis='6-31G',
                      scf='qc')

def _read_charges(fd):
    fd.readline()
    qs = []
    ms = []
    for line in fd:
        if not line.strip()[0].isdigit():
            break
        qs.append(float(line.split()[2]))
        if len(line.split()) > 3:
            ms.append(float(line.split()[3]))
    return {'charges': qs, 'magmoms': ms} if ms else {'charges': qs}

print(hf.get_initial_charges())
#print(_read_charges(fd))
#for i in range(len(atoms)): #distances for each atom in the molecule
#        print(f"mass {i} : {atoms.calc.results['charges']}")
