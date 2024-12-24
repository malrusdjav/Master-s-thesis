#bs = ['6-31g', 'cc-pvdz', '3-21g', 'sto-3g'] #basis sets
bs = ['6-31g'] #basis sets
exc_corr = ['b3lyp','pbe0'] #exchange correlation
#exc_corr = ['b3lyp'] #exchange correlation

for curr_basis in bs:
   for  curr_corr in exc_corr:
      Nbasis='             N library '+curr_basis
      Hbasis='             H library '+curr_basis
      input_parse('basis; '+Nbasis+'; '+Hbasis+'; end')
      input_parse('dft; xc '+curr_corr+'; iterations 100; end')
      e=task_energy('dft');print(e)
      print('DFT with xc=',curr_corr,' and with basis=',curr_basis,' gives energy=',e)
