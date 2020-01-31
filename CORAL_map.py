import numpy as np
import scipy

def CORAL_map(Xs,Xt):
    Ds = Xs.copy()
    Dt = Xt.copy()
    
    #print(np.sum(np.isnan(Ds)), np.sum(np.isnan(Dt)))
        
    cov_src = np.ma.cov(Ds.T) + np.eye(Ds.shape[1])
    cov_tar = np.ma.cov(Dt.T) + np.eye(Dt.shape[1])
    
    #A_coral = np.dot(cov_src**(-1/2), cov_tar**(1/2))
        
    Cs = scipy.linalg.sqrtm(np.linalg.inv(np.array(cov_src)))
    Ct = scipy.linalg.sqrtm(np.array(cov_tar))
    
    #Cs[np.isnan(Cs)] = 0
    #Ct[np.isnan(Ct)] = 0
    #print(np.sum(np.isnan(Cs)), np.sum(np.isnan(Ct)))
    #print(np.sum(np.isnan(Cs)), Cs.shape[0]*Cs.shape[1])
    A_coral = np.dot(Cs, Ct)
    #print(np.sum(np.isnan(A_coral)), A_coral.shape[0]*A_coral.shape[1])
    #print(A_coral)
    #print(np.dot(Ds, A_coral))
    
    #Ds[np.isnan(Ds)] = 1
    Xs_new = np.dot(Ds, A_coral)
    #print(Xs_new)
    return Xs_new