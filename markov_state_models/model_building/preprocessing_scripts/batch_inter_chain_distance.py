import mdtraj as md
import numpy as np
import itertools

import pyemma
from os.path import isfile
import numpy as np
from glob import glob

chain_contact = pyemma.coordinates.featurizer('SH3_Ubq_Solv_6_eq_nowater.pdb')

ubq_ = chain_contact.select('resid 0 to 75 and not type H ')
sh3_ = chain_contact.select('resid 76 to 150 and not type H ')

chain_contact.add_group_mindist([ubq_, sh3_], periodic=False)

for fn in glob('joined_strided_trajectories/trajectory_*.xtc'):
  out_fn = fn[:-4]+"_cf.npz"
  if isfile(out_fn):
    print('{} already computed. Skipping ...'.format(out_fn))
    continue
  else:
    print('Computing {}  ...'.format(out_fn))
    chain_c_source = pyemma.coordinates.source([fn] , chain_contact)
    data_ = chain_c_source.get_output()
    np.savez(out_fn, data_[0])


#
#  def strisint(s):
#      try:
#          int(s)
#          return True
#      except ValueError:
#          return False
#
#
#  k=0
#  poelse=[]
#  temporary_=[]
#  for i,data in source.iterator(stride=5):
#      if i>k:
#          #assemble trajectory fragments
#          joined = np.concatenate(temporary_)
#          # move to origin
#          joined = joined - joined.mean(axis=1, keepdims = True)
#          #reshape and transform, take only first PC
#          poelse.append(pca.transform(joined.reshape((joined.shape[0], 280*3)) )[:, 0]  )
#          temporary_=[data]
#          k=i
#      else:
#          temporary_.append(data)
#
##assemble trajectory fragments
#  joined = np.concatenate(temporary_)
## move to origin
#  joined = joined - joined.mean(axis=1, keepdims = True)
##reshape and transform, take only first PC
#  poelse.append(pca.transform(joined.reshape((joined.shape[0], 280*3)) )[:, 0]  )
#
#  for i,pinc in enumerate(poelse):
#    np.save(f'_model/pincer_mode_{i}.npz', pinc)
