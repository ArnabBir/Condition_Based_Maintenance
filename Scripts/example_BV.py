from numpy import *
from decimal import *
from sys import *
import numpy as np
import pandas as pd


#if len(argv) != 2:
    #print "required input: trainfile testfile"
    #assert(False)
#argv = []
#argv.append(pd.read_csv('D:\Github\Open_IIT_DA\Datasets\d1h1.csv'))
#argv.append(pd.read_csv('D:\Github\Open_IIT_DA\Datasets\d1h2.csv'))
#argv.append(pd.read_csv('D:\Github\Open_IIT_DA\Datasets\d11h2.csv'))

#train_file = argv[1]
#test_file = argv[2]
train_file = 'D:\Github\Open_IIT_DA\Datasets\d1h2.csv'
test_file = 'D:\Github\Open_IIT_DA\Datasets\d11h5.csv'
def number(arg):
    return Decimal(arg)

def sampledict(sett):
 DPdict = dict()
 for sequence in sett:
     if DPdict.has_key(tuple(sequence)):
         DPdict[tuple(sequence)] = DPdict[tuple(sequence)] + 1
     else:
         DPdict[tuple(sequence)] = 1
 return DPdict

def normalize(arr):
 sumarr = number(sum(arr))
 if sumarr != 0.0:
     for i in range(len(arr)):
         arr[i] = arr[i] / sumarr
 else:
     for i in range(len(arr)):
         arr[i] = 1.0 / number(len(arr))

def sampleprobabilities(sett, DPdict):
 probs = []
 for sequence in sett:
     probs.append(number(DPdict[tuple(sequence)]) / number(len(sett)))
 return probs

def threegramdict(sett):
 DPdict = dict()
 total = 0
 for sequence in sett:
     ngramseq = [-1,-1] + sequence.split() + [-2]
     for start in range(len(ngramseq)-2):
         total
         end = start + 2
         if DPdict.has_key(tuple(ngramseq[start:end])):
             table = DPdict[tuple(ngramseq[start:end])]
             if table.has_key(ngramseq[end]):
                 table[ngramseq[end]] = table[ngramseq[end]] + 1
             else:
                 table[ngramseq[end]] = 1
             table[-1] = table[-1] + 1
         else:
             table = dict()
             table[ngramseq[end]] = 1
             table[-1] = 1
             DPdict[tuple(ngramseq[start:end])] = table
 return DPdict

def threegramprobabilities(sett,DPdict):
 probs = []
 for sequence in sett:
     prob = number('1.0')
     ngramseq = [-1,-1] + sequence.split() + [-2]
     for start in range(len(ngramseq)-2):
         end = start + 2
         prob = prob * (number(DPdict[tuple(ngramseq[start:end])][ngramseq[end]]) / number(DPdict[tuple(ngramseq[start:end])][-1]))
     probs.append(prob)
 return probs

def readset(f):
 sett = []
 line = f.readline()
 l = line.split(" ")*
 num_strings = int(l[0])
 alphabet_size = int(l[1])
 for n in range(num_strings):
     line = f.readline()
     l = line.split(" ")
     sett = sett + [[int(i) for i in l[1:len(l)]]]
 return alphabet_size, sett

def writeprobs(probs,f):
 f.write(str(len(probs)) + "\n")
 for i in range(len(probs)):
	if(probs[i]==0):
		print i
	f.write(str(probs[i]) + "\n")

alphabet, test = pd.read_csv('D:\Github\Open_IIT_DA\Datasets\d11h2.csv')
alphabet, train = pd.read_csv('D:\Github\Open_IIT_DA\Datasets\d1h2.csv')

sampleprobs = sampleprobabilities(test,sampledict(train+test))
threegramprobs = threegramprobabilities(test,threegramdict(train+test))

normalize(sampleprobs)
normalize(threegramprobs)

writeprobs(sampleprobs, open(test_file+".txt","w"))
writeprobs(threegramprobs, open(test_file+".txt","w"))