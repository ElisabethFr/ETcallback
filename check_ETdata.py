"""
file to load eyetracking data and do some plots
Oct 2023
Author: Elisabeth Freund
Human Brain Mapping Lab at Feinstein Institutes for Medical Research

This script is intended to give a starting point to handling the eyetracking data resulting from my gaze callback.
Most efficient data handling might be to deal with the hdf5 file throughout the entire pipeline (results in lower memory usage).
However, it is also possible to load all data into a pandas dataframe (see below).
Examples of accessing data in this script are indexing directly into the hdf5 file.
"""
import os
import h5py
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt
plt.interactive(True)


datadir = 'C:\\Users\lisaf\Documents\git\ETcallback\\test'
file = 'test1_eyetrackerData.h5'
path = os.path.join(datadir, file)

# read data
with h5py.File(path, 'r') as io:
    data = io['ETdata'][:]
    colnames = io['ETdata'].attrs['headers'][:]

# create pandas dataframe of eyetracking data
ETdata = pd.DataFrame(data=data,columns=colnames)

# plot how the timestamps develop
data = np.array(data)
plt.figure()
plt.plot(data[:,0])

# check how many gaze points are valid
print('percentage of valid gaze points left eye: ' + str((sum(data[:, 14])/data.shape[0])*100))
print('percentage of valid gaze points right eye: ' + str((sum(data[:, 29])/data.shape[0])*100))
print('percentage of timestamps with both eyes valid: ' + str(sum(data[:, 14]+data[:, 29] == 2)/data.shape[0]))
print('percentage of timestamps with no valid gaze points: ' + str(sum(data[:, 14]+data[:, 29] == 0)/data.shape[0]))

# plot where subject looked (averaged between right and left eye)
plt.figure()
gaze = np.transpose(np.array([(data[:, 12] + data[:, 27])/2, (data[:, 13] + data[:, 28])/2]))
plt.plot(gaze[:, 0], gaze[:, 1], marker='.', linewidth=0, markersize=1)
