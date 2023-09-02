N = int(input())
A, P, X = [], [], []
for _ in range(N):
    a, p, x = map(int, input().split())
    A.append(a)
    P.append(p)
    X.append(x)

tmp = 10**9
for i in range(N):
    if X[i] - A[i] > 0: # 1台ずつ減るところはこれでいい
        tmp = min(tmp, P[i])
    
print(tmp if tmp != 10**9 else -1)
