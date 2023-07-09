N, D = map(int, input().split())
T = list(map(int, input().split()))

ans = -1
for i in range(N - 1): # N-1まで
    if T[i + 1] - T[i] <= D:
        ans = T[i + 1]
        break

print(ans)
