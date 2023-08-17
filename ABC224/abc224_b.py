H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

flag = True
for i1 in range(0, H, 1):
    for i2 in range(i1, H, 1):
        for j1 in range(0, W, 1):
            for j2 in range(j1, W, 1):
                if A[i1][j1]+A[i2][j2] > A[i2][j1]+A[i1][j2]: # 成り立たなかったら終了
                    flag = False
                    break

print("NYoe s" [flag::2])
