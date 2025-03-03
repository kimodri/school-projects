from array_structure import Array

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
myArr.insert(7)
myArr.insert(6)
print(myArr.size)
print(myArr.search(10))
print(myArr.size)


print([x for x in myArr._array])
print(list(myArr.sort()))
print(list(myArr.sort(reversed=True)))
print(myArr.size)

print(myArr.size)
myArr.delete(7) # nakapag pa zero ng self.size?!
print(myArr.size)
print([x for x in myArr._array])




