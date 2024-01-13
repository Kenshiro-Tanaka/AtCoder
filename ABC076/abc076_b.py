N = int(input())
K = int(input())

tmp = 1
for i in range(N):
    tmp = min(2*tmp, tmp+K)

print(tmp)
