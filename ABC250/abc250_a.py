H, W = map(int, input().split())
R, C = map(int, input().split())

cnt = 0
for i in range(1, H + 1): # R, Cは1スタートだから合わせたい
    for j in range(1, W + 1):
        if abs(i - R) + abs(j - C) == 1:
            cnt += 1

print(cnt)
