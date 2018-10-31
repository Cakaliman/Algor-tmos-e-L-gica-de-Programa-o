m = int(input('Tamanho do vetor A: '))
a = [0] * m
for i in range(m):
    x = int(input(f'Elemento da posição {i}: '))
    a[i] = x

n = int(input('Tamanho do vetor B: '))
b = [0] * n
for j in range(n):
    y = int(input(f'Elemento da posição {j}: '))
    b[j] = y
print(a)
print(b)

c = a + b
print(c)

