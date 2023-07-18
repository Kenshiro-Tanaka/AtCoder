N, X = map(int, input().split())
A = list(map(int, input().split()))

l = [0] * N # 知っているかどうかのリスト
for _ in range(N):
    l[X - 1] = 1 # 知ったから1にする
    X = A[X - 1] # 次に教える相手はAから決まる

print(l.count(1))
