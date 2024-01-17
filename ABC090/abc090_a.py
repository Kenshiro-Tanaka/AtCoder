c = [input() for i in range(3)]

tmp = ""
for i in range(len(c)):
    tmp += c[i][i]

print(tmp)
