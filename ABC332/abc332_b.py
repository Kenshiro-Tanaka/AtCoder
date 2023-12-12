K, G, M = map(int, input().split())

Glass = 0
Mug = 0
for i in range(K):
    if Glass == G:
        Glass = 0
    elif Mug == 0:
        Mug = M
    else:
        tmp = min(Mug, G-Glass)
        Mug -= tmp
        Glass += tmp

print(Glass, Mug)
