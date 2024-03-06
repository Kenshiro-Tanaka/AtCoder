N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = [-1]*N # あとで変えるのでとりあえず -1
for i in A:
    ans[i-1] = 0 # 花火が上がる日は 0

for i in range(N-1, -1, -1): # 後ろから見ていくから
    if ans[i] != 0:
        ans[i] = ans[i+1] + 1 # この式でいい

for i in ans:
    print(i)
