N = int(input())
A = [list(input()) for _ in range(N)]

flag = True # 矛盾があったらFalseに
for i in range(N):
    for j in range(N):
        if A[i][j] == "W" and A[j][i] != "L":
            flag = False
            break
        elif A[i][j] == "L" and A[j][i] != "W":
            flag = False
            break
        elif A[i][j] == "-" and A[j][i] != "-":
            flag = False
            break

print("correct" if flag else "incorrect")
