N = int(input())
H = list(map(int, input().split()))

tmp, cnt = 0, 0
for i in range(N):
    if H[i] >= tmp:
        cnt += 1
    tmp = max(tmp, H[i])

print(cnt)
