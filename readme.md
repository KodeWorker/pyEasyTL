# pyEasyTL

## Introduction
This project is the reimplementation of EasyTL in Python.
The EasyTL paper on the [website](http://transferlearning.xyz/code/traditional/EasyTL/) show this domain adaptation method is intuitive and parametric-free.
The MATLAB source code is on this [Repo](https://github.com/jindongwang/transferlearning/tree/master/code/traditional/EasyTL).

- We use scipy.optimize.linprog instead of PuLP suggested in the paper
- M^(-1/2) = (M^(-1))^(1/2) = scipy.linalg.sqrtm(np.linalg.inv(np.array(cov_src)))

## Dev Log
- **2020/1/31** CORAL_map still has some issue. (fixed)
- **2020/1/31** The primitive results of Amazon dataset show that we'v successfully implemented the EasyTL(c).