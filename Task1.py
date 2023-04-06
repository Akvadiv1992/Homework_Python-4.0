from random import randint
n = int(input("введите количество элементов 1 множества: "))
array_1 = [0] * n
for i in range(n):
    array_1[i] = randint(0, 10)
print(array_1)

m = int(input("введите количество элементов 2 множества: "))
array_2 = [0] * m
for i in range(m):
    array_2[i] = randint(0, 10)
print(array_2)

s = sorted(set(array_1).intersection(array_2))
print("числа, которые встречаются в обоих наборах:", end=" ")
print(*s)