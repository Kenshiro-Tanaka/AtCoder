A, B, K = map(int, input().split())

ans = 0 
while A < B:  # AがB未満なら続ける
    A *= K
    ans += 1

print(ans)
