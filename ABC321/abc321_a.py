N = list(input())

d = len(N)
ans = "Yes"
for i in range(d-1):
    if N[i] <= N[i+1]:
        ans = "No"

print(ans)
