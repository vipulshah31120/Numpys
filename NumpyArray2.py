#Array creation using numpy methods :
#numpy.empty(shape, dtype = float, order = ‘C’)

import numpy as np
a = np.empty(2, dtype=int)
print('Matrix a: \n', a)

b = np.empty([2, 2], dtype=int)
print('Matrix b: \n',b )

c = np.empty([3, 3])
print('\n Matrix c: \n', c)



# numpy.zeros method

a = np.zeros(2, dtype=int)
print('Matrix a: \n',a)

b = np.zeros([2, 3], dtype=int)
print('Matrix b: \n', b)




# numpy.reshape() method

array = np.arange(8)
print('Original Array: \n', array)

array = np.arange(8).reshape(2, 4)
print('\n  Array Reshaped with 2 rows & 4 columns: \n',array)

array = np.arange(8).reshape(2, 2, 2)
print('\n Original Array reshaped to 3D: \n', array)



#numpy.arange method

print('A\n', np.arange(4).reshape(2, 2), '\n')

print('A\n', np.arange(4, 10), '\n')

print('A\n', np.arange(4, 20, 3), '\n')



# numpy.linspace method
print("B\n", np.linspace(2, 3, num=5, retstep=True), "\n")

x = np.linspace(0, 2, 10)
print("A\n", np.sin(x))



# numpy.flatten() method

array = np.array([[1, 2], [3, 4]])
array.flatten()
print(array)

array.flatten('F')
print(array)
