N, M, P = map(int, input().split())

cnt = 0
day = M
while day <= N:
    day += P
    cnt += 1

print(cnt)
