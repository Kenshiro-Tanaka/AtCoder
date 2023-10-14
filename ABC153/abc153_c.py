N, K = map(int, input().split())
H = list(map(int, input().split()))

if N > K: # 大きい順にK個を0にして残ったものの和
    sH = sorted(H, reverse=True)
    for i in range(K):
        sH[i] = 0
    print(sum(sH))
else:
    print(0)
