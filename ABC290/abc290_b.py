N, K = map(int, input().split())
S = input()

ans = ''
cnt = 0 # K人で打ち切りたい
for c in S:
    ans += c
    if c == 'o':
        cnt += 1
    if cnt == K:
        break

while len(ans) < N: # 打ち切った後xで埋めたい
    ans += 'x'

print(ans)
