N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))
# D[i]の皿はP[i+1]円，ただしDに無ければP[0]円

ans = 0
for i in C:
    if i in D:
        idx = D.index(i)
        ans += P[idx+1]
    else:
        ans += P[0]

print(ans)
