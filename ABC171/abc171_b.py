N, K = map(int, input().split())
p = list(map(int, input().split()))

P = sorted(p)
sum = 0
for i in range(K):
    sum += P[i]

print(sum)
