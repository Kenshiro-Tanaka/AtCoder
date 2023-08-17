N, K = map(int, input().split())
S = [input() for _ in range(N)]

l = sorted(S[:K])
for i in l:
    print(i)
