import numpy as np
import sys 
plist=[1,2,3,4,5]
narray=np.array([1,2,3,4,5])
lsize=sys.getsizeof(plist) + sum(sys.getsizeof(i) for i in plist)
asize=narray.nbytes
print("Size of list:",lsize,"Bytes")
print("Size of Array:",asize,"Bytes")