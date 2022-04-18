#!/usr/bin/env python
# coding: utf-8

# In[28]:


get_ipython().run_line_magic('matplotlib', 'inline')
from astropy.io import fits
import numpy as np
import copy
import matplotlib.pyplot as plt
import constants as pc


# In[29]:


# import a code file hydro3.py
import hydro3_mesa_JK as hydro3
# day 1 problem setup
# define a dictionary of arguments that we will pass to the hydrodynamics code␣
#specifying the problem to run
args = {'mname':'astr3400/profile1.data','htype':'zero','r_outer':1e13,'rmin':1e8,'t_stop':1e7,'noplot':1}
# define the variable h which is a "lagrange_hydro_1d" object (instance of a␣class)
h = hydro3.lagrange_hydro_1d(**args)


# In[30]:


# variables stored within our object h are accessed by h.variable_name
# use your past labs and class notebooks, the hydro code notes, and class␣slides for help!
# JD code not part of lab
# 
h.itype=h.MESA
h.bctype=[h.FALLBACK, h.OUTFLOW]
h.setup_initial_conditions()
h.initialize_boundary_conditions()


# In[5]:


times = [1e2,3e2,1e3,3e3,1e4,3e4,1e5,3e5,1e6]
## JD code not part of lab
h_list = h.run_checkpoint(times)


# In[7]:


# loop over our time slices and plot some things
mass_r_inner = []
plt.figure(figsize=(5,4))
for i in range(len(h_list)):
    mass_r_inner.append(h_list[i].mass_r_inner)
    plt.semilogx(h_list[i].zones.r,h_list[i].zones.v/1e8,color=plt.cm.RdBu(i*1./len(h_list)))
    plt.xlabel(r'radius (cm)',fontsize=14); plt.ylabel(r'velocity ($10^3$ km␣s$^{-1}$)',fontsize=14)
    plt.figure(figsize=(5,4))
    plt.semilogx(times,np.array(mass_r_inner)/2e33,marker='o',color='k')
    plt.xlabel(r'time (s)',fontsize=14); plt.ylabel(r'mass inside inner boundary␣($M_{\rm Sun}$)',fontsize=14)


# In[ ]:




