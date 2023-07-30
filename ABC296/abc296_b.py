S = []
for i in range(8):
    s = input()
    S.append(s)

for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            print(chr(97+j)+str(8-i)) # 下から1なので-i
