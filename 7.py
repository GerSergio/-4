import random
print("Введите количество чисел в массиве A(целое число)")
n=int(input())
a=[]
for i in range(n):
    x=random.randint(0,25)
    a.append(x)
print("Массив А:",a)
print()
print("Введите количество чисел в массиве B(целое число)")
h=int(input())
b=[]
for j in range(h):
    x=random.randint(0,25)
    b.append(x)
print("Массив В:",b)
print()
ans=[]
for k in range(n):
    for g in range(h):
        if(a[k]==b[g]):
            ans.append(a[k])
new=list(set(ans))#удаление повторяющихся элементов
if(len(new)!=0):
    print("Решение:")
    print(new)
else:
    print("Нет одинаковыз элементов :(")

