N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]

mat = [[False]*N for _ in range(N)] # 不仲判定行列
for i in range(M):
    for j in range(N-1):
        mat[a[i][j]-1][a[i][j+1]-1] = True # 右隣をTrueに
        mat[a[i][j+1]-1][a[i][j]-1] = True # 左隣をTrueに
        if i == j:
            mat[i][j] = False

cnt = 0
for i in range(N):
    for j in range(i+1, N, 1):
        if i != j and mat[i][j] == False: # 右上三角行列だけ見たい
            cnt += 1

print(cnt)
