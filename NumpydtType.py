import numpy as np


dt  = np.dtype('>i4')
print('Byte Order is: ', dt.byteorder)
print('Size is : ', dt.itemsize)
print('DataType is: ', dt.name)