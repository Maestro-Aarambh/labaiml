import time
import numpy as np
plist1=[i for i in range(10000000)]
plist2=[i for i in range(10000000)]
narray1=np.array(plist1)
narray2=np.array(plist2)
pres=[]
pstime=time.perf_counter()
for i in range(1000):
    pres.append(plist1[i]+plist2[i])
petime=time.perf_counter()
nstime=time.perf_counter()
nres=narray1+narray2
netime=time.perf_counter()
print("Time for list actions ",(petime-pstime),"seconds")
print("Time for array action",(netime-nstime),"seconds")