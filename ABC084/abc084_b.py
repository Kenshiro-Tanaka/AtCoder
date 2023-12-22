A, B = map(int, input().split())
S = input()

flag = True
if S[A] != "-":
    flag = False
else:
    if "-" in S[:A] or "-" in S[A+1:]:
        flag = False

print("NYoe s"[flag::2])
