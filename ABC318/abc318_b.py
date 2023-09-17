N = int(input())
sheet = [[0]*100 for _ in range(100)] # [[0]*100]*100 は浅いコピーなので値がコピーされてしまう
for i in range(N):
    a, b, c, d = map(int, input().split())
    for j in range(a, b, 1):
        for k in range(c, d, 1):
            sheet[j][k] = 1 # 覆っていれば1に
    
S = 0
for j in range(100):
    for k in range(100):
        if sheet[j][k]: # 覆っていれば面積として
            S += 1

print(S)
