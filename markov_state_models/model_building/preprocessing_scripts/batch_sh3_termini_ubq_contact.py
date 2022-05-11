import mdtraj as md
import numpy as np
import itertools

import pyemma
from os.path import isfile
import numpy as np
from glob import glob

chain_contact = pyemma.coordinates.featurizer('SH3_Ubq_Solv_6_eq_nowater.pdb')

ubq_ = chain_contact.select('resid 0 to 75 and not type H ')
sh3_ = chain_contact.select('((resid 76 to 90) or (resid 140 to 150)) and not type H ')

chain_contact.add_group_mindist([ubq_, sh3_], periodic=False)

for fn in glob('joined_strided_trajectories/trajectory_*.xtc'):
  out_fn = fn[:-4]+"_sh3tu.npz"
  if isfile(out_fn):
    print('{} already computed. Skipping ...'.format(out_fn))
    continue
  else:
    print('Computing {}  ...'.format(out_fn))
    chain_c_source = pyemma.coordinates.source([fn] , chain_contact)
    data_ = chain_c_source.get_output()
    np.savez(out_fn, data_[0])


