N = int(input())

l = []
for a in range(2, 10**5+1, 1):
    b = 2
    while a**b <= N:
            l.append(a**b)
            b += 1

print(N-len(list(set(l)))) # 2^4と4^2みたいな被りがある
