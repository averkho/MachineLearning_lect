# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:10:07 2021

@author: AVERKHO
"""

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

X1=[(-1,2),(-2,1),(-1,0),(-1,1)]
z1=(-1,1)
X2=[(2,1),(3,2)]
z2=(2,2)

def eucliduan_distance(x,z):
    '''
    

    Parameters
    ----------
    x : Point - tuple.
    z : Point - tuple.

    Returns
    -------
    Euclidian distance between two points

    '''
    
    return np.sqrt((x[0]-z[0])**2+(x[1]-z[1])**2)