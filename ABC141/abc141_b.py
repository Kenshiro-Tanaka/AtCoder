S = input()

flag = True
for i in range(len(S)):
    if i%2 == 0:
        if S[i] not in ["R", "U", "D"]:
            flag = False
            break
    else:
        if S[i] not in ["L", "U", "D"]:
            flag = False
            break

print("NYoe s"[flag::2])
