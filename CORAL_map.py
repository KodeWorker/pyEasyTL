import numpy as np

def CORAL_map(Xs,Xt):
    cov_src = np.cov(Xs) + np.eye(Xs.shape[1]);
    cov_tar = np.cov(Xt) + np.eye(Xt.shape[1]);
    print(cov_src.shape, cov_tar.shape)
    A_coral = cov_src^(-1/2) * cov_tar^(1/2);
    Xs_new = np.dot(Xs, A_coral)
    return Xs_new