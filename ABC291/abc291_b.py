N = int(input())
X = list(map(int, input().split()))

# max，minで探してもいいけど並び替えて最後と最初を消していってもいい
l = sorted(X)
for i in range(N):
    del l[-1]
    del l[0]

print(sum(l)/len(l))

# 別解 ループも消す必要もない
# X.sort()
# print(sum(X[N:4*N])/len(N:4*N))
