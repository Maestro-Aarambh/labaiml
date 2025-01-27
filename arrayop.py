import numpy as np
arr=np.array([1,2,3,4,5])
a=int(input("1.for array type,2.for array axes,3.for array shap,4.for array element type:"))
if a==1:
    print("Array Type is:",type(arr))
elif a==4:
    print("Type of element in arra is:",arr.dtype)
elif a==2:
    print("Axis of array is:",arr.ndim)#ndim to check for dimension or axis
elif a==3:
    print("Shape of array is:",arr.shape)#shape used for number of elements in array
else:
    print("Invalid choice entred")
