import itertools

N, M = map(int, input().split())
x = []
for _ in range(M):
    l = list(map(int, input().split()))
    x.append(l[1:]) # k使わない

flag = [[False]*N for _ in range(N)] # これが全部Trueになればよい
for i in range(N):
    flag[i][i] = True # 自分は除く

for i in range(M):
    for combi in itertools.permutations(x[i], 2):
        flag[combi[0]-1][combi[1]-1] = True

print("Yes" if flag == [[True]*N]*N else "No") # コピーしないので[[True]*N]*Nの書き方でいい
