# Common libs
import time
import numpy as np
import pickle
import torch
import math
from multiprocessing import Lock
# OS functions
from os import listdir
from os.path import exists, join, isdir

# Load batch_limit dictionary
batch_lim_file = join('C:\\DLCode\\KPConvPrj\\Data\\S3DIS\\PKL', 'neighbors_limits.pkl')
if exists(batch_lim_file):
    with open(batch_lim_file, 'rb') as file:
        batch_lim_dict = pickle.load(file)
DD=0
