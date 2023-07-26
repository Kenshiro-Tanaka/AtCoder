N = int(input())
S = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(1, 1000, 1):
        a = (S[i] - 3 * j) / (4 * j + 3)
        if a > 0 and int(a) == a: # 整数であるかの判定
            cnt += 1
            break # 1個でも見つかればok

print(N - cnt) # 誤りの人数なので
