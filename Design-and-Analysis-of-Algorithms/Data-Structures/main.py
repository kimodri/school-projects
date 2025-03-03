from data_structure import Array

myArr = Array("i")


myArr.insert(2)
myArr.insert(4)
myArr.insert(9)
myArr.insert(1)
myArr.insert(7)
myArr.insert(8)
myArr.insert(3)
myArr.insert(5)
myArr.insert(0)
myArr.insert(6)



print([x for x in myArr._array])
print(list(myArr.sort()))
print(list(myArr.sort(reversed=True)))

print(myArr.search(1))
print(myArr.search(11))
print(myArr.search(69))


