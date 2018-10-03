def primo(n):
    ac = 0
    for c in range(1, n+1):
        if n%c==0:
             ac = ac + 1
    if ac == 2:
        print(bool(1))
    else:
        print(bool(0))

x = int(input('x: '))
primo(x)
print('--FIM--')