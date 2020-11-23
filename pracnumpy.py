import numpy as np
p1=np.array([10,20,30,40])
print('Single dimensional array: ',p1)
pb=np.array([30,40])
pn=np.array([20,10])
print(np.sum([pb,pn]))
print(np.sum([pb,pn],axis=0))
print(np.sum([pb,pn],axis=1))
print(np.vstack([pb,pn]))
print(np.hstack([pb,pn]))
print(np.column_stack([pb,pn]))
p2=np.array([[10,20,30],[12,24,36]])
print('Multi-dimensional array: ',p2)
p3=np.zeros((1,2))
print("Array with 1 row and 2 cols with zero as value: ",p3)
p4=np.zeros((6,6))
print("Array with 6 rows and 6 cols with zero as value: ",p4)
p5=np.full((3,3),10)
print("Array with 3*3 dimensions and value as 10 : ",p5)
p6=np.arange(1,10)#skip parameter is 1
print("Arrays with values: ",p6)
p7=np.arange(1,10,5)#skip parameter is 5
print(p7)
p8=np.random.randint(10,20,5)
print(p8)
p9=np.shape([[1,2,3],[4,5,6]])
print(p9)
p10=np.array([[1,2,3],[4,5,6]])



