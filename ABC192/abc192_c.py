def g1(x):
    l = [int(i) for i in list(str(x))] # 桁ごとのリストを作る
    l.sort(reverse = True)
    L = int("".join(map(str, l))) # joinはstrにしてから
    return L

def g2(x):
    l = [int(i) for i in list(str(x))]
    l.sort()
    L = int("".join(map(str, l)))
    return L

def f(x):
    return g1(x) - g2(x)

N, K = map(int, input().split())

a = N
for i in range(K):
    a = f(a)

print(a)
