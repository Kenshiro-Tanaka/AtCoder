N = int(input())
ans = 0
for _ in range(N):
    a = list(input().split()) # split()しないと1文字ずつになる
    ans += int(a[0]) if a[1] == "JPY" else float(a[0])*380000.0
    
print(ans)
