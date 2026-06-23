# x = lambda a, b: a+b
# print(x(1,2))
# y = map(lambda b: b+1, [1,2,3,4])
# print(list(y))
# import functools as ft
# y = ft.reduce(lambda b,a: b+1, [1,2,3,4])
# print(y)

# gen = (x+1 for x in range(6))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# def doub(x):
#     return x*2
# y = map(doub, [1,2,3,4])
# print(list(y))
import math
arr= [1,2,1]
ot = [1]
n = 4

for i in range(0, math.ceil(n/2)):
    print(arr[i:i+2])
    print(sum(arr[i:i+2]))
    ot.append(sum(arr[i:i+2]))
ot.append(1)
print(ot)