import glob
import numpy as np
import os
import shutil

"""
Small script to take a part of the cats-and-dogs dataset and split it into train, val and test sets. 
"""


np.random.seed(42)

""" Load data """

files = glob.glob('data/train/*')

catFiles = [fn for fn in files if 'cat' in fn]
dogFiles = [fn for fn in files if 'dog' in fn]
print(len(catFiles), len(dogFiles))

""" Create random datasets """

catTrain = np.random.choice(catFiles, size=1500, replace=False)
dogTrain = np.random.choice(dogFiles, size=1500, replace=False)
catFiles = list(set(catFiles) - set(catTrain))
dogFiles = list(set(dogFiles) - set(dogTrain))

catVal = np.random.choice(catFiles, size=500, replace=False)
dogVal = np.random.choice(dogFiles, size=500, replace=False)
catFiles = list(set(catFiles) - set(catVal))
dogFiles = list(set(dogFiles) - set(dogVal))

catTest = np.random.choice(catFiles, size=500, replace=False)
dogTest = np.random.choice(dogFiles, size=500, replace=False)

print('Cat datasets:', catTrain.shape, catVal.shape, catTest.shape)
print('Dog datasets:', dogTrain.shape, dogVal.shape, dogTest.shape)

""" Save datasets """

trainDir = 'trainingData'
valDir = 'validationData'
testDir = 'testData'

trainFiles = np.concatenate([catTrain, dogTrain])
validateFiles = np.concatenate([catVal, dogVal])
testFiles = np.concatenate([catTest, dogTest])

os.mkdir(trainDir) if not os.path.isdir(trainDir) else None
os.mkdir(valDir) if not os.path.isdir(valDir) else None
os.mkdir(testDir) if not os.path.isdir(testDir) else None

for fn in trainFiles:
    shutil.copy(fn, trainDir)

for fn in validateFiles:
    shutil.copy(fn, valDir)

for fn in testFiles:
    shutil.copy(fn, testDir)
