H, N = map(int, input().split())
A = list(map(int, input().split()))

flag = False
sA = sorted(A, reverse=True)
for i in range(N):
    H -= sA[i]
    if H <= 0:
        flag = True
        break

print("NYoe s"[flag::2])
