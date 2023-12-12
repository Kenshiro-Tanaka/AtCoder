N, S, K = map(int, input().split())
ans = 0
for i in range(N):
    p, q = map(int, input().split())
    ans += p*q
    
print(ans+K if ans < S else ans)
