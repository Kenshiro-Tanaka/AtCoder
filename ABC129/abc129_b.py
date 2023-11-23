N = int(input())
W = list(map(int, input().split()))

# S1は前から入れていく，S2は後ろから入れていく
rW = list(reversed(W))
S1, S2, x, y = 0, 0, 0, 0 # xはWの前からいくつかか，yはrWの前からいくつかか
for _ in range(N):
    if S1 <= S2:
        S1 += W[x]
        x += 1
    else:
        S2 += rW[y]
        y += 1

print(abs(S1-S2))
