# パスカルの三角形
N = int(input())

a = [[0] * N for i in range(N)] # 2次元配列の初期化はこうしないとダメ
for i in range(N):
    for j in range(N):
        if i < j:
            a[i][j] = 0
        elif j == 0 or j == i:
            a[i][j] = 1
        else:
            a[i][j] = a[i-1][j-1]+a[i-1][j]
        
        if a[i][j] != 0:
            print(a[i][j], end=" ")
    print("\n", end="") # end以降を入れないと2回改行が入っちゃう


# 2次元配列の初期化について，id()を使って調べてみる
# a = [[0]*N]*N と書くとアドレスが一致したN個の配列ができるため1箇所の変更が全てに適用されてしまう
# shallow copy と deep copy
