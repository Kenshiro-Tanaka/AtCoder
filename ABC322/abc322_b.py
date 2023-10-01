N, M = map(int, input().split())
S = input()
T = input()
 
print(0 if (S == T[:N] and S == T[-N:]) else 1 if (S == T[:N] and S != T[-N:]) else 2 if (S != T[:N] and S == T[-N:]) else 3)
