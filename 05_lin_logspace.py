import numpy as np
a = np.linspace(10, 20, 5) #切5等份 print(a)
# endpoint = False, 切5+1=6等份,最後一個等份不要 a = np.linspace(10, 20, 5, endpoint = False) print(a)
a = np.linspace(10, 20, 6, endpoint = True)
print(a)
b = np.linspace(0, 2, 9).reshape(3,3)
print(b)
#以2為底, 次方從0到9,分成10等份 c = np.logspace(0, 9, 10, base=2, dtype='i4').reshape(2,5) print (c)
