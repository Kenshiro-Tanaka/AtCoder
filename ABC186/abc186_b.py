H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

tmp = 101 # 一番少ない基準のブロック数になる
for i in range(H):
    for j in range(W):
        if A[i][j] <= tmp:
            tmp = A[i][j]

cnt = 0 # 取り除くブロック数のカウント
for i in range(H):
    for j in range(W):
        cnt += A[i][j] - tmp

print(cnt)
