N = int(input())
A = list(map(int, input().split()))
S, T = [], []
for i in range(N-1):
    s, t = map(int, input().split())
    S.append(s)
    T.append(t)

for i in range(N-1):
    num = A[i]//S[i] # 左から繰り返せる回数分繰り返していけばいい
    A[i] -= S[i]*num
    A[i+1] += T[i]*num

print(A[-1])
