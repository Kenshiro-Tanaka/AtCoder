N, W = map(int, input().split())
A = list(map(int, input().split()))
AA = [0] + A # これをしないと1番目だけを選ぶパターンなどが含まれない

tmp = []
if N >= 3:
    for i in range(N+1):
        for j in range(i+1, N+1, 1):
            for k in range(j+1, N+1, 1):
                tmp.append(AA[i]+AA[j]+AA[k])
if N >= 2:
    for i in range(N+1):
            for j in range(i+1, N+1):
                tmp.append(AA[i]+AA[j])
if N >= 1:
    for j in range(N+1):
        if i != 0:
            tmp.append(AA[i])

tmp = list(filter(lambda x: x <= W, tmp))    
print(len(set(tmp)))
