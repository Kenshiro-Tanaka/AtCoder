N, X = map(int, input().split())
L = list(map(int, input().split()))

D, cnt = 0, 1
for i in range(N):
    D += L[i]
    if D > X:
        break
    else:
        cnt += 1

print(cnt)
