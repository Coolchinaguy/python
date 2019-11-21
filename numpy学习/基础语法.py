import numpy as np

a = np.array([1,2,3])
print(a)

#不止一个维度

aa = np.array([[1,2],[3,4]])
print(aa)

aaa = np.array([1,2,3,4,5],ndmin=2)
print(aaa)

b = np.array([1,2,3],dtype = complex) #dtype是数据类型
print(b)

dt = np.dtype(np.int32)
print(dt)

dt1 = np.dtype("i4")
print(dt1)

dt2 = np.dtype('>i4')
print(dt2)

dt3 = np.dtype([('age',np.int8)])
print(dt3)

dt4 = np.dtype([('age',np.int8)])
c =np.array([(10,),(20,),(30,)],dtype= dt4)
print(c)
print(c['age'])

student = np.dtype([('name','S20'),('age','i1'),('marks','<f4')])
d = np.array([('abc',21,50),('xyz',18,75)],dtype = student)
print(student)
print(d)