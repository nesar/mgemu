import numpy as np
import pickle
from sklearn.decomposition import PCA
import gpflow

class emu:
    
#    def __init__(self):

#        self.GPmodelFile = "models/GPflow_model_213Smooth_rank16snap97"
#        self.PCAmodelFile = "models/PCAmodelFile"
#        self.para_array = np.array([0.14, 0.88, 0.8, 1e-6, 2])
#        self.gpmodel = gpmodel
#        self.pcamodel= pcamodel

    def scale01(self, fmin, fmax, f):
        return (f - fmin) / (fmax - fmin)

    def load_models(self, GPmodelFile, PCAmodelFile):
        ctx_for_loading = gpflow.saver.SaverContext(autocompile=False)
        saver = gpflow.saver.Saver()
        self.gpmodel = saver.load(GPmodelFile, context=ctx_for_loading)
        self.gpmodel.clear()
        self.gpmodel.compile()

        self.pcamodel = pickle.load(open(PCAmodelFile, 'rb'))
        return self.gpmodel, self.pcamodel

    def predict(self, para_array):
        gpm = self.gpmodel.predict_f(para_array)  #[0] is the mean and [1] the predictive
        W_predArray = gpm[0]
        W_varArray = gpm[1]
        return W_predArray, W_varArray

    def emulate(self, para_array):
        kvals = np.loadtxt('./data/kvals.txt')
        lhdmin, lhdmax = np.loadtxt('./data/paralims.txt')
        
        if ((para_array < lhdmin).any() or (para_array > lhdmax).any() ):
            print('WARNING:input cosmology parameters outside range of the emulator. Extrapolation may not be accurate')
        
        if len(para_array.shape) == 1:
            para_array_rescaled = self.scale01(lhdmin, lhdmax, para_array)
            W_predArray, _ = self.predict(np.expand_dims(para_array_rescaled, axis=0))
            x_decoded = self.pcamodel.inverse_transform(W_predArray)
            return kvals, np.squeeze(x_decoded)#[0]
