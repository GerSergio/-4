import random
print("Введите количество чисел в массиве(целое число)")
n=int(input())
print()
a=[]
for i in range(n):
    x=random.uniform(1,100)
    a.append(x)
print("Массив а :",)
print(a)
print()
cou=0
d=max(a)
print("Максимальный элемент массива а :",)
print(d)
print()
for j in range(n):
    if(a[j]==d):
        cou=j
        break
for k in range(cou+1,n):
    a[k]=0
print("Решение :")
print(a)









