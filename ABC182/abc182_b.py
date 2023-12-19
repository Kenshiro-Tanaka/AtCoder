N = int(input())
A = list(map(int, input().split()))

GCD = [0]*(max(A)+1)
for i in range(1, max(A)+1, 1):
    for j in A:
        if j%i == 0:
            GCD[i] += 1

tmp, ans = 0, 0
for i, v in enumerate(GCD[2:]):
    if v >= tmp:
        tmp = v
        ans = i+2

print(ans)
