S = input()

flag = True
if int(S[:4]) < 2019:
    flag = False
elif int(S[5:7]) < 5:
    flag = False

print("TBD" if flag else "Heisei")
