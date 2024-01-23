N = int(input())
W = [input() for _ in range(N)]

flag = True
if len(set(W)) != N:
    flag = False
else:
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            flag = False

print("NYoe s"[flag::2])
