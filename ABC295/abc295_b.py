import copy # deepcopyを使うため

R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]

A = copy.deepcopy(B) # 二次元配列のコピーはdeepcopy
for i in range(R): # (i,j)は爆弾の位置
    for j in range(C):
        if '1' <= B[i][j] <= '9':
            for m in range(R): # 爆発が届くか調べたい位置(m,n)
                for n in range(C):
                    if abs(i-m)+abs(j-n) <= int(B[i][j]):
                        A[m][n] = '.'
                    
for m in range(R): # 指定された表示形式
    for n in range(C):
        print(A[m][n], end="")
    print()
