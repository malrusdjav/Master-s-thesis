%mem=1GB
%chk=MyJob.chk
%save
#P b3lyp/6-31G ! ASE formatted method and basis
scf(qc)

Gaussian input prepared by ASE

0 1
H                 0.0000000000        0.0000000000        0.0000000000
H                 0.0000000000        0.0000000000        0.7400000000


