import math

K = int(input())

ans = 0
for a in range(1, K+1, 1):
    for b in range(1, K+1, 1):
        for c in range(1, K+1, 1):
            ans += math.gcd(a, b, c) # gcd(a, b, c) = gcd(gcd(a, b), c)

print(ans)

# gcd()をユークリッドの互除法でやる方法をC++で
