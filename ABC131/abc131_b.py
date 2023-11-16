N, L = map(int, input().split())

l = [] # おいしさリストは単調増加
for i in range(N):
    l.append(L+i)
n_pi = sum(l)

if 0 in l:
    print(n_pi) # 0を通るなら0を引くと1番差が小さい
elif L > 0:
    print(n_pi-L) # 要素が全て正なら最初を引くと1番差が小さい
else:
    print(n_pi-l[N-1]) # 要素が全て負なら最後を引くと1番差が小さい
