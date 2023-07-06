N = int(input())
l = [list(map(str, input().split())) for i in range(N)]

# 一番若い人のindexが欲しい
tmp = 10**10 # Aの最大値より1桁多い
ind = 0
for i in range(N):
    if tmp > int(l[i][1]):
        tmp = int(l[i][1])
        ind = i
    
L = l[ind:] + l[:ind]

# この書き方できるのか
for name, age in L:
    print(name)


# 別解
# m = min(A)
# ind = A.index(m) 重複していないならindexが一意に返ってくる
# S.extend(S) Sの後ろにSを追加して円卓に
# for i in range(ind, ind + N):
#     print(S[i])
