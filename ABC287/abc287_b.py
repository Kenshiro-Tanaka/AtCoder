N, M = map(int, input().split())
S, T = [], []
for _ in range(N):
    s = input()
    S.append(s)
for _ in range(M):
    t = input()
    T.append(t)

cnt = 0
for i in range(N):
    for j in range(M):
        if S[i].endswith(T[j]):
            cnt += 1
            break # 大意よりS[i]は「いずれかに一致」すればいいので

print(cnt) 
