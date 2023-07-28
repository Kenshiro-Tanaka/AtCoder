H, W = map(int, input().split())

cnt = 0
for _ in range(H):
    s = input()
    for j in s:
        if j == '#':
            cnt += 1

print(cnt)
