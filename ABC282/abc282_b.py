N, M = map(int, input().split())
S = [input() for i in range(N)]

cnt = 0
for x in range(N-1):
    for y in range(x+1, N, 1):
        flag = True
        for j in range(M):
            if S[x][j] == "x" and S[y][j] == "x": # x番目とy番目の人のどちらかで"o"であり続ければいい
                flag = False
                break
        if flag: # 全部の問題で flag = True なら cnt += 1
            cnt += 1

print(cnt)
