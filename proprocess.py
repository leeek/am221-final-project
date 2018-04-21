import numpy as np
import pandas as pd

def read_data(filename, size=None):
    if size is not None:
        df = pd.read_csv('data/' + filename, header=None, size=size)
    else:
        df = pd.read_csv('data/' + filename, header=None)
    label = df.iloc[:,0].as_matrix()
    data = df.iloc[:,1:].as_matrix()
    return label, data
