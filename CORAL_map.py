import numpy as np
import scipy

def CORAL_map(Xs,Xt):
    Ds = Xs.copy()
    Dt = Xt.copy()
      
    cov_src = np.ma.cov(Ds.T) + np.eye(Ds.shape[1])
    cov_tar = np.ma.cov(Dt.T) + np.eye(Dt.shape[1])
       
    Cs = scipy.linalg.sqrtm(np.linalg.inv(np.array(cov_src)))
    Ct = scipy.linalg.sqrtm(np.array(cov_tar))
    A_coral = np.dot(Cs, Ct)
    
    Xs_new = np.dot(Ds, A_coral)
    return Xs_new