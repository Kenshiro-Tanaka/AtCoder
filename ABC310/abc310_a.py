N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

ans = P
for i in range(N):
    ans = min(ans, Q + D[i]) # こう書けば必ず最小値が最後に残る

print(ans)
