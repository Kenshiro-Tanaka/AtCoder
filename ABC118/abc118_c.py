N = int(input())
A = list(map(int, input().split()))

l = A # 答えのindexを求める用のコピー
for _ in range(N-1):
    tmp = [] # そのループでの勝者を入れていく
    for j in range(0, len(A), 2):
        tmp.append(max(A[j], A[j+1]))
    del A # len(A)で新たに回したいのでAを消してtmpを入れる
    A = tmp

print(l.index(min(A))+1) # 準優勝なので小さい方
