N = int(input())
D, X = map(int, input().split())
ans = 0
for i in range(N):
    a = int(input())
    for j in range(1, D+1, a):
        ans += 1

print(ans+X)
