#!/usr/bin/env python
# coding: utf-8

"""
    
    Gaussian Process Emulator for the ratio of Dark matter power spectra in Modified Gravity Cosmology and $\Lambda$CDM Cosmology r(k; Cosmology)
    
    The cosmological paramters currently supported are {Omega_m, n_s, sigma_8, f_R_0, n}
"""

from mgemu import emu
import numpy as np

# The Sample models below are trained for $z=0.01999$. Other models will be updated soon (and a $z$ dependence in the emulator will be implemented as well)

mgCosmo = emu() # Calling a emulator instant
mgCosmo.load_models(GPmodelFile='models/GPflow_model', PCAmodelFile='models/PCA_model') # Loading relevant models


paraCosmos = np.array([0.14, 0.88, 0.8, 1e-6, 2]) # Test cosmology parameters: Omega_m, n_s, sigma_8, f_R_0, n
ks, rCosmo = mgCosmo.emulate(paraCosmos) # Output: k, r(k)

print(ks, rCosmo)

