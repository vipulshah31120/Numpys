#Array creation using array functions :
#array(data type, value list)

import array
arr = array.array('i', [1, 2, 3])

print('The New Created Array is: ', end=' ')
for i in range(0, 3) :
    print(arr[i], end=' ')

print('\r')
