N = int(input())
C = [] # 賭けた目の個数を保存
A = [] # 賭けた目を保存，二次元配列に
for i in range(N):
    c = int(input())
    C.append(c)
    a = list(map(int, input().split()))
    A.append(a)
X = int(input())

tmp = 38 # C <= 37なので超過していればなんでもよい
for i in range(N):
    if X in A[i]: # 賭けている人で
        tmp = min(tmp, len(A[i])) # 賭けた個数が一番少ないもの

cnt = 0
ans = []
for i in range(N):
    if X in A[i] and C[i] == tmp: # 賭けている人かつ賭けた個数が一番少ない人
        cnt += 1
        ans.append(i+1)

print(cnt)
print(*ans)
