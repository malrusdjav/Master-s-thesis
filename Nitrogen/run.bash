#!/bin/bash

proj=N2_hf_ccpvdz_geopt

echo "running nwchem job for project=$proj"

mpirun -np 4 /usr/bin/nwchem  $proj.nw > $proj.out
