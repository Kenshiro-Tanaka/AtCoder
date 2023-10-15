S = list(input())

N = len(S)
flag = True # 満たさない条件があったらFalseに

# Sは回文 -> 逆にしても同じ
Sr = list(reversed(S))
if S != Sr:
    flag = False

# S[0:(N-1)//2]も回文
S1 = S[0:(N-1)//2]
S1r = list(reversed(S1))
if S1 != S1r:
    flag = False

# S[(N+3)//2-1:N+1]も回文
S2 = S[(N+3)//2-1:N+1] # index的に-1
S2r = list(reversed(S2))
if S2 != S2r:
    flag = False

print("NYoe s"[flag::2])
