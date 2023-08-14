N = int(input())
S, T = [], []
for _ in range(N):
    s, t = map(str, input().split())
    S.append(s)
    T.append(t)

flag = False
for i in range(N):
    for j in range(N):
        if i != j: # これがなきゃ1つ目で必ずTrueに
            if S[i] == S[j] and T[i] == T[j]:
                flag = True
                break

print("NYoe s" [flag::2])
