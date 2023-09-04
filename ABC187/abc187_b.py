N = int(input())
x, y = [], []
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

cnt = 0
for i in range(N):
    for j in range(i, N): # i < jの分減らせる
        if x[j] != x[i]: # 忘れていた条件
            if -1 <= (y[j]-y[i])/(x[j]-x[i]) <= 1:
                cnt += 1

print(cnt)
