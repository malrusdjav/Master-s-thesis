
from ase.db import connect

db = connect('database.db')
for row in db.select():
    atoms = row.toatoms()
    print(atoms)

