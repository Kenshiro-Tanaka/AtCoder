N = int(input())

S = []
for _ in range(N):
    c = input()
    S.append(c)

for i in range(N - 1, -1, -1):
    print(S[i])
    
