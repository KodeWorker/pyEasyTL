import numpy as np
from CORAL_map import CORAL_map
from label_prop import label_prop

def get_class_center(Xs,Ys,Xt,dist):
	
    source_class_center = np.array([])
    Dct = np.array([])
    for i in np.unique(Ys):
        sel_mask = Ys == i
        X_i = Xs[sel_mask.flatten()]
        mean_i = np.mean(X_i, axis=0)
        if len(source_class_center) == 0:
            source_class_center = mean_i.reshape(-1, 1)
        else:
            source_class_center = np.hstack((source_class_center, mean_i.reshape(-1, 1)))
		
        if dist == "ma":
            print("not implemented yet!")
        elif dist == "euclidean":
            Dct_c = np.sqrt(np.nansum((mean_i - Xt)**2, axis=1))
        elif dist == "sqeuc":
            print("not implemented yet!")
        elif dist == "cosine":
            print("not implemented yet!")
        elif dist == "rbf":
            print("not implemented yet!")
        if len(Dct) == 0:
            Dct = Dct_c.reshape(-1, 1)
        else:
            Dct = np.hstack((Dct, Dct_c.reshape(-1, 1)))
    
    return source_class_center, Dct

def EasyTL(Xs,Ys,Xt,Yt,intra_align="coral",dist="euclidean",lp="linear"):
# Inputs:
#   Xs          : source data, ns * m
#   Ys          : source label, ns * 1
#   Xt          : target data, nt * m
#   Yt          : target label, nt * 1
# The following inputs are not necessary
#   intra_align : intra-domain alignment: coral(default)|gfk|pca|raw
#   dist        : distance: Euclidean(default)|ma(Mahalanobis)|cosine|rbf
#   lp          : linear(default)|binary

# Outputs:
#   acc         : final accuracy
#   y_pred      : predictions for target domain
    
# Reference:
# Jindong Wang, Yiqiang Chen, Han Yu, Meiyu Huang, Qiang Yang.
# Easy Transfer Learning By Exploiting Intra-domain Structures.
# IEEE International Conference on Multimedia & Expo (ICME) 2019.

	C = len(np.unique(Ys))
	if C > np.max(Ys):
		Ys += 1
		Yt += 1
	
	m = len(Yt)
	
	if intra_align == "raw":
		print('EasyTL using raw feature...')
	elif intra_align == "pca":
		print('EasyTL using PCA...')
	elif intra_align == "gfk":
		print('EasyTL using GFK...')
	elif intra_align == "coral":
		print('EasyTL using CORAL...')
		Xs = CORAL_map(Xs, Xt)
	
	_, Dct = get_class_center(Xs,Ys,Xt,dist)
	print('Start intra-domain programming...')
	Mcj = label_prop(C,m,Dct,lp)
	y_pred = np.argmax(Mcj, axis=1) + 1
	acc = np.mean(y_pred == Yt.flatten());

	return acc, y_pred
	
