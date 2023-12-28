H, M = list(map(int, input().split()))

def judge(H, M):
    H = str(H)
    M = str(M)
    # 先行ゼロを追加
    if len(H) < 2:
        H = "0" + H
    if len(M) < 2:
        M = "0" + M
    # 判定
    if 0 <= int(H[0]+M[0]) <= 23 and 0 <= int(H[1]+M[1]) <= 59:
        print(H, M)
        exit()

for i in range(1000):
    if (M+i)%60 == 0: # 00分を超えるたびに H に1を足す
        H += 1
    judge(H%24, (M+i)%60)
