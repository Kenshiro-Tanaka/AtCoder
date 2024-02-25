N = int(input())
P = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    a, b = map(int, input().split())
    print(a if P.index(a) < P.index(b) else b)
