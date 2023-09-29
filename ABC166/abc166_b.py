N, K = map(int, input().split())
l = [0]*N # 持っているかどうか
for i in range(K):
    int(input()) # d使わない
    a = list(map(int, input().split()))
    for j in range(len(a)):
        l[a[j]-1] += 1

print(l.count(0))
