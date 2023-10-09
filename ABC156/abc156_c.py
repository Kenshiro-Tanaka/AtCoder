N = int(input())
X = list(map(int, input().split()))

ans = 100000000000
for P in range(100):
    wa = 0
    for i in range(N):
      wa += (X[i]-P)*(X[i]-P)  
    ans = min(ans, wa)

print(ans)
