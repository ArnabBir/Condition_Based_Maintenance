import pandas as pd
from hmmlearn import hmm
from hmmlearn import base
import numpy as np
from sklearn.externals import joblib
#import matplotlib.pyplot as plt
from matplotlib import cm, pyplot as plt
import math
import loglikelihood

np.random.seed(123)

hval = [21,20,20,16,19,18,21,19,23,23,23,21,45,44]
data = []
#count = 0
for i in range(14):
    for j in range(hval[i]):
        #data.append(pd.read_csv('D:\Github\Open_IIT_DA\Datasets\d' + str(i+1) + 'h' + str(j + 1) + '.csv'))
        data.append(pd.read_csv('D:\Github\Open_IIT_DA\Data\Filename_d' + str(i+1) + 'h' + str(j + 1) + '.csv'))
        #count += 1
        #data[i] = scale(data[i])
#data = pd.concat(data)
remodel = hmm.GaussianHMM(n_components= 3, covariance_type="full", n_iter=500).fit(data[2])
#print data[1]
#remodel.startprob_ = np.array([0.6, 0.3, 0.1]
#remodel.transmat_ = np.array([[0.7, 0.2, 0.1],[0.3, 0.5, 0.2], [0.3, 0.3, 0.4]])
#remodel.means_ = np.array([[0.0, 0.0], [3.0, -3.0], [5.0, 10.0]])
#remodel.covars_ = np.tile(np.identity(2), (3, 1, 1))
#data[1], Z = model.sample(100)
#print data[2]
pval = [] 
hidden_states = remodel.predict(data[36])
#p = 1
#remodel.fit(data[2])
#print remodel
##fig, axs = plt.subplots(remodel.n_components, sharex=True, sharey=True)
#plt.show()
#base._BaseHMM._init(data[1])
#print "ll = " + str(base._BaseHMM._compute_log_likelihood(data[1]))
print("Means and vars of each hidden state")
for i in range(remodel.n_components):
    print("{0}th hidden state".format(i))
    print("mean = ", remodel.means_[i])
    print("var = ", np.diag(remodel.covars_[i]))
    #print()

#fig, axs = plt.subplots(remodel.n_components, sharex=True, sharey=True)
#colours = cm.rainbow(np.linspace(0, 1, remodel.n_components))
#for i, (ax, colour) in enumerate(zip(axs, colours)):
    # Use fancy indexing to plot data in each state.
    #mask = hidden_states == i
    #ax.plot_date(dates[mask], close_v[mask], ".-", c=colour)
    #ax.set_title("{0}th hidden state".format(i))

    # Format the ticks.
    #ax.xaxis.set_major_locator(YearLocator())
    #ax.xaxis.set_minor_locator(MonthLocator())

    #ax.grid(True)

f = open('Hidden.txt', 'w')
for i in hidden_states:
	f.write(str(i) + " ")
f.close()
#plt.show()
print "remodel = " + str(remodel.monitor_.converged)
#loglh =  loglikelihood.llr(np.matrix(remodel.transmat_))
#print loglh

for itr in xrange(0,21):
	#remodel = hmm.GaussianHMM(n_components=3, covariance_type="diag", n_iter=500).fit(data[itr])
	Z = remodel.predict(data[itr])
	#joblib.dump(remodel, "filename.pkl")
	#print Z
	#print remodel.transmat_
	print Z
	p = 1
	for i in xrange(len(Z)-1):
		p *= remodel.transmat_[Z[i]][Z[i+1]]
	pval.append(math.log(p))
	#loglh =  loglikelihood.llr(np.matrix())
	#print loglh
	print math.log(p)
	#print p
#for itr in xrange(0,len(pval)-1):
#	pval[itr] = pval[itr]+pval[itr+1]
#	pval[itr] = pval[itr]/2

pval_mean = np.mean(pval)
pval_sd = np.std(pval)
y = np.linspace(1,len(pval), len(pval))
plt.plot(y,pval)
plt.plot(pval_mean-pval_sd)
plt.show()
#print "pval_mean = " + str(pval_mean)
#print "pval_sd = " + str(pval_sd)
#threshold = -19.355
threshold = pval_mean 
th1 = -19.355
print "Th = " + str(threshold)
state = []
for i in pval:
	if i > threshold:
		state.append("EX")
	else:
		state.append("NO")
print state
f = open('states2.txt', 'ab')
#for i in state:
f.write('\n' + str(state))
f.close()
print remodel.transmat_
remodel.transmat_[Z[1]][Z[2]]
