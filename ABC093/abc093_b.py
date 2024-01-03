A, B, K = map(int, input().split())

l = []
for i in range(K):
    if A+i <= B:
        l.append(A+i)
    if A <= B-i:
        l.append(B-i)

l = sorted(set(l))

for i in range(len(l)):
    print(l[i])
