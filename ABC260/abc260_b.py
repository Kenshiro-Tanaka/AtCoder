N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

people = [False]*N

if X != 0:
    dA = {i:A[i] for i in range(len(A))} # indexも保持したいので辞書で
    sorted_dA = sorted(dA.items(), key=lambda x:x[1], reverse=True)
    for i in range(X):
        people[sorted_dA[i][0]] = True

if Y != 0:
    dB = {i:B[i] for i in range(len(B))}
    sorted_dB = sorted(dB.items(), key=lambda x:x[1], reverse=True)
    cnt = 0 # 合格となっていない受験者の中で考えなおすために
    for i in range(N):
        if people[sorted_dB[i][0]] == False:
            people[sorted_dB[i][0]] = True
            cnt += 1
        if cnt == Y:
            break

if Z != 0:
    dC = {i:A[i]+B[i] for i in range(N)}
    sorted_dC = sorted(dC.items(), key=lambda x:x[1], reverse=True)
    cnt = 0
    for i in range(N):
        if people[sorted_dC[i][0]] == False:
            people[sorted_dC[i][0]] = True
            cnt += 1
        if cnt == Z:
            break

for i in range(N):
    if people[i]:
        print(i+1)
