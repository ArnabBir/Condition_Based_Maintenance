import pandas as pd
from hmmlearn import hmm
import numpy as np
from sklearn.externals import joblib
#import matplotlib.pyplot as plt
from matplotlib import cm, pyplot as plt
import math
import loglikelihood

np.random.seed(42)

hval = [21,20,20,16,19,18,21,19,23,23,23,21,45,44]
data = []
#count = 0
for i in range(14):
    for j in range(hval[i]):
        data.append(pd.read_csv('D:\Github\Open_IIT_DA\Datasets\d' + str(i+1) + 'h' + str(j + 1) + '.csv'))
        #count += 1
        #data[i] = scale(data[i])
#data = pd.concat(data)
remodel = []
remodel.append(hmm.GaussianHMM(n_components=2, covariance_type="diag", n_iter=500).fit(data[1]))
remodel.append(hmm.GaussianHMM(n_components=2, covariance_type="diag", n_iter=500).fit(data[2]))
remodel.append(hmm.GaussianHMM(n_components=2, covariance_type="diag", n_iter=500).fit(data[]))
remodel.append(hmm.GaussianHMM(n_components=2, covariance_type="diag", n_iter=500).fit(data[1]))




for i in hval:


