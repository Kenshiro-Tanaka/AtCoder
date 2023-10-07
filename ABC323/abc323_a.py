S = input()

flag = True
for i in range(1, 16):
    if i%2 != 0:
        if S[i] != "0":
            flag = False
            break

print("NYoe s"[flag::2])
