def g1(x):
    x = str(x) # 桁ごとに分けるには int -> str -> list
    l = list(x)
    l.sort(reverse = True)
    return int("".join(l))

def g2(x):
    x = str(x)
    l = list(x)
    l.sort()
    return int("".join(l))

def f(x):
    return g1(x) - g2(x)

N, K = map(int, input().split())

a = N
for i in range(K):
    a = f(a)

print(a)
