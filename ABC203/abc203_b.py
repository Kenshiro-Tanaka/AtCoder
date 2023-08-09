N, K = map(int, input().split())

ans = 0
for i in range(N):
    for j in range(K):
        ans += (i+1)*100 + (j+1) # 'i0j'は 100i+j，ただし0始まりなので+1する

print(ans)
