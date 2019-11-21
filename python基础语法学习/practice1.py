'''基础数据结构'''

a,b,c = 1,2,"john"

print(a,b,c)

str = 'hello world'

print(str)

print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + " TEST")


#列表（允许更新）
list = ['abcd',784,2.23,'john',70.2]
tinylist = [123,'john']

print(list)
print(list[0])#和字符串操作方法基本一致
print(list + tinylist)

#元组（不允许更新）
tuple = ('abcd',786,2,23,'john',70.2)
tinytuple = (123,'john')

print(tuple)
print(tuple[0])#和字符串操作方法基本一致
print(tuple + tinytuple)

#字典（组成：健（key）：值（value）

dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"

tinydict = {'name':'john','code':6734,'dept':'sales'}

print(dict['one'])
print(dict[2])
print(tinydict)#输出完整的字典
print(tinydict.keys())#输出所有键
print(tinydict.values())#输出所有值