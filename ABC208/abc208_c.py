N, K = map(int, input().split())
a = list(map(int, input().split()))

n = K//N # 均等に分け与えた分
K_prime = K - n*N
sa = sorted(a)
v = sa[K_prime] # 余りを前から何人渡すか考えるための閾値
for i in range(N):
    print(n if a[i] >= v else n+1)
