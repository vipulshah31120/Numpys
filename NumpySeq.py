import numpy as np

arr = np.arange(10, 1, -2)
print(arr)

newarr = arr[np.array([3, 1, 2])]
print(newarr)

a = np.arange(20)
print('a[-8 : 17 : 1] : ', a[-8:17:1])              # -8 starts from right end of the array

b = np.array([[[1, 2, 3], [4, 5, 6]],
             [[7, 8, 9], [10, 11, 12]]])
print(b[..., 1])                                    # Ellipsis (…) is the number of : objects needed to make a
                                                    # selection tuple of the same length as the dimensions of the array.

c = np.array([[1, 2], [3, 4], [5, 6]])
print(c[[0, 1, 2], [0, 0, 1]])                      # Each element of first dimension is paired with the element of the
                                                    # second dimension. So the index of the elements in this case are
                                                    # (0,0),(1,0),(2,1) and the corresponding elements are selected.

d = np.array([[5, 5], [4, 5], [16, 4]])
sumrow = d.sum(-1)                                  # select those elements whose sum of row is a multiple of 10.
print(d[sumrow%10==0])


e1 = 10
e2 = 11

num = np.bitwise_and(e1, e2)
print(num)

f1 = [2, 8, 125]
f2 = [3, 3, 115]

num2 = np.bitwise_and(f1, f2)
print(num2)