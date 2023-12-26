N, Q = map(int, input().split())
a = [[] for _ in range(N)]
for i in range(N):
    a[i] = list(map(int, input().split()))

for _ in range(Q):
    s, t = map(int, input().split())
    print(a[s-1][t])
