N, X = map(int, input().split())
alc = 0
for i in range(N):
    v, p = map(int, input().split())
    alc += v*p # 浮動小数点で誤差が出て WA になるため式変形をして整数で比較する
    if alc > 100*X:
        print(i+1)
        exit()

print(-1)
