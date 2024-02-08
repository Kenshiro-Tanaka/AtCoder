input()
S = list(input())

x, ans = 0, 0
for i in S:
    x = x+1 if i == "I" else x-1
    ans = max(ans, x)

print(ans)
