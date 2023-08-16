N = int(input())
S = [input() for _ in range(N)]

bun_l = []
for i in S:
    for j in S:
        if i != j:
            bun_l.append(i + j)

flag = False
for bun in bun_l:
    cnt = 0 # 判定用，その文が回文であれば長さと一致する
    for i in range(len(bun)):
        if bun[i] == bun[len(bun)-i-1]:
            cnt += 1
    if cnt == len(bun):
        flag = True
        break
    
print("NYoe s" [flag::2])
