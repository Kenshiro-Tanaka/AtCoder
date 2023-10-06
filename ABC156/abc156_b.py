N, K = map(int, input().split())

ans = 0
while N >= K: # n桁なら，N // (Kのn-1乗) = 1
    N //= K
    ans += 1

print(ans+1) # Kの0乗分
