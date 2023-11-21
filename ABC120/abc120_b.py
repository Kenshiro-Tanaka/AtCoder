A, B, K = map(int, input().split())

l = [] # 約数リスト
for i in range(1, 101, 1):
    if A%i == 0 and B%i == 0:
        l.append(i)

sl = sorted(l, reverse=True)
print(sl[K-1])
