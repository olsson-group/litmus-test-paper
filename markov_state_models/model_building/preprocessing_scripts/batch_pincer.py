import mdtraj as md
import numpy as np

import pyemma
import itertools
from os.path import isfile

def strisint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

traj0=md.load('traj_noPBC/SH3_Ubq_Solv_0_eq_prod_nowater_nopbc.xtc', top="SH3_Ubq_Solv_6_eq_nowater.pdb")[:2]


#compute pincer basis
xtal_ubq = md.load('ubi_xray46_fit.pdb')

xtal_ubq.superpose(traj0, atom_indices=xtal_ubq.topology.select('(name CA or name C or name N ) and resid 0 to 69'), ref_atom_indices=traj0.topology.select('(name CA or name C or name N ) and resid 0 to 69') )

heavy_bb = xtal_ubq.topology.select('(name CA or name C or name N ) and resid 0 to 69')
CA_bb = xtal_ubq.topology.select('name CA and resid 0 to 69')
traj_heavy_bb = traj0.topology.select('(name CA or name C or name N ) and resid 0 to 69')

bb_xyz_origin = xtal_ubq.xyz[:,heavy_bb,:] - xtal_ubq.xyz[:,heavy_bb,:].mean(axis=1, keepdims=True)
bb_xyz_origin_traj0 = traj0.xyz[:,traj_heavy_bb,:] - traj0.xyz[:,traj_heavy_bb,:].mean(axis=1, keepdims=True)
bb_xyz_feat=bb_xyz_origin.reshape((46,210*3))

traj0_bb_xyz_feat=bb_xyz_origin_traj0.reshape((bb_xyz_origin_traj0.shape[0],210*3))
from sklearn.decomposition import PCA
pca=PCA(10, whiten=True)
pca=pca.fit(bb_xyz_feat)

# get trajectory filenames
fix_trajn = [i for i in range(786) if isfile('traj_noPBC/SH3_Ubq_Solv_%i_eq_prod_nowater_nopbc.xtc'%i) ]
traj_filenames = [f'traj_noPBC/SH3_Ubq_Solv_{i}_eq_prod_nowater_nopbc.xtc' for i in fix_trajn]
from glob import glob

file_names= [f"joined_strided_trajectories/trajectory_{i}.xtc" for i in range(1015)]


ca = pyemma.coordinates.featurizer('SH3_Ubq_Solv_6_eq_nowater.pdb')
ca.add_selection(ca.select('(name CA or name C or name N ) and resi 0 to 69'))

source = pyemma.coordinates.source(file_names, features=ca)

k=0
poelse=[]
temporary_=[]
for i,data in source.iterator(stride=1):
    if i>k:
        #assemble trajectory fragments
        joined = np.concatenate(temporary_)
        # move to origin
        joined = joined - joined.mean(axis=1, keepdims = True)
        #reshape and transform, take only first PC
        poelse.append(pca.transform(joined.reshape((joined.shape[0], 210*3)) )[:, 0]  )
        temporary_=[data]
        k=i
    else:
        temporary_.append(data)

#assemble trajectory fragments
joined = np.concatenate(temporary_)
# move to origin
joined = joined - joined.mean(axis=1, keepdims = True)
#reshape and transform, take only first PC
poelse.append(pca.transform(joined.reshape((joined.shape[0], 210*3)) )[:, 0]  )

for i,pinc in enumerate(poelse):
  np.save(f'_model/pincer_mode_{i}.npz', pinc)
