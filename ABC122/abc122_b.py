S = list(input())
 
n = 0 # 候補となる文字列の長さ
for i in range(len(S)):
    tmp = ""
    for j in S[i:]: # 開始位置を i で変える
        if j in ["A", "C", "G", "T"]:
            tmp += j
            n = max(n, len(tmp))
        else:
            tmp = ""
            break

print(n)
