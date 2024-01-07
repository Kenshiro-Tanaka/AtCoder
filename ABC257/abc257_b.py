# Pawnはチェスで一番弱いコマ，将棋でいう歩兵

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

# L番目のコマが動かせるかどうか
for i in range(Q):
    if A[L[i]-1] != N: # マスの一番右ではないとき
        if A[L[i]-1] == max(A): # 見ているものが右端であるなら移動できる
            A[L[i]-1] += 1 # 右に1つ移動
        else:
            if A[L[i]] - A[L[i]-1] != 1: # 右端でないときA[L[i]]は存在する
                A[L[i]-1] += 1 # 右に1つ移動

print(*A)
