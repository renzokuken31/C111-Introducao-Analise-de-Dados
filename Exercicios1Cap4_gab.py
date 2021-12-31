import numpy as np
# 1
'''
arr = np.linspace(0,1,21)
print(arr)
'''

#2 e #3
'''
par = np.arange(0,51,2)
par2 = np.arange(100,50,-2)
print(par)
print(par2)
print(np.sort(np.concatenate((par,par2))))
print(np.flip(np.sort(np.concatenate((par,par2)))))
'''

#4
'''
mtz = np.ones([3,4])
print(mtz)
arr = mtz.reshape(12)
print(arr)
'''

#5
mtz = np.array([[3,4,1],[5,6,2],[7,8,3]])
print(mtz)
if (mtz.shape[0] * mtz.shape[1])%2 == 0:
    print('Pode se tornar um vetor par')
else:
    print('Pode se tornar um vetor impar')