## Emulator for p(k) ratio for modified gravity models

Minimal working example

```
from mgemu import emu
import numpy as np


# Calling an emulator instance
mgCosmo = emu()

# Loading trained PCA and GP models
mgCosmo.load_models(GPmodelFile='models/GPflow_model', PCAmodelFile='models/PCA_model') 

# Specify cosmological parameters: Omega_m, n_s, sigma_8, f_R_0, n
paraCosmos = np.array([0.14, 0.88, 0.8, 1e-6, 2]) 

# Retrieve emulated r(k) = P_MG(k)/P_LCDM(k) 
ks, rCosmo = mgCosmo.emulate(paraCosmos) # Output: k, r(k)

```
