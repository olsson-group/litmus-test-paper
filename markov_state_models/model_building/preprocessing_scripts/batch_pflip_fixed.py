import mdtraj as md
import numpy as np

import pyemma
import itertools
from os.path import isfile


def remap_phi_psi(phi, psi):
    """
    Compute peptide-flip angle in ubiquitin according to Smith et al 2017
    """
    rphi = (phi*180/np.pi+360)%360
    rpsi = (psi*180/np.pi+360)%360
    orange = np.where((rphi+rpsi)>350)
    rpsi[orange] = rpsi[orange]-360
    return rpsi-rphi
    

def strisint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


file_names= [f"joined_strided_trajectories/trajectory_{i}.xtc" for i in range(1015)]

print(file_names)

ca = pyemma.coordinates.featurizer('align_topol.pdb')
ca.add_backbone_torsions('resi 51 to 52')


k=0
poelse=[]
temporary_=[]
for i,fn in enumerate(file_names): 
  print(fn)
  data = pyemma.coordinates.load(fn, features=ca)
  pinc=remap_phi_psi(data[:,2], data[:,1])
  np.save(f'_model/pepflip_{i}.npz', pinc)
