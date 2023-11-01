S = list(input())

flag = True
if S.count(S[0]) != 2:
    flag = False
if S.count(S[1]) != 2:
    flag = False
if S.count(S[2]) != 2:
    flag = False
if S.count(S[3]) != 2:
    flag = False

print("NYoe s"[flag::2])
