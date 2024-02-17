S = list(input())

# 正答となるパターンは2通り
S = [int(i) for i in S]
l0, l1 = [], []
for i in range(len(S)):
    l0.append(i%2)
    l1.append((i+1)%2)

cnt = 0
for i in range(len(S)):
    if S[0] == 0:
        if S[i] != l0[i]:
            cnt += 1
    else:
        if S[i] != l1[i]:
            cnt += 1

print(cnt)
