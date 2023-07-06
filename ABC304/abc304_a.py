N = int(input())
l = [list(map(str, input().split())) for i in range(N)]

# 一番若い人のindexが欲しい
tmp = 10**10 # Aの最大値より1桁多い
index = 0
for i in range(N):
    if tmp > int(l[i][1]):
        tmp = int(l[i][1])
        index = i
    
L = l[index:] + l[:index]

# この書き方できるのか
for name, age in L:
    print(name)
