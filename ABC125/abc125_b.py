N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
for i in range(N):
    if V[i]-C[i] > 0: # 正のものだけ足し続ければ X-Y は大きくなっていく
        ans += V[i]-C[i]

print(ans)
