A, B, C, D = map(int, input().split())

flag = False
n = 0
if C*D != B:
    while n < A/(C*D-B):
        n += 1
        if n >= A/(C*D-B):
            flag = True
            break
        else:
            flag = False
            if n >= 10000000: # 適当に大きい数字
                break
        
print(n if flag else -1)

# 水色がA+nB個，赤色がnC個だからA+nB <= nCDとなったら終了
# つまりA <= n(CD-B)より n >= A/(CD-B)

# 傾きと切り上げを使った別解をC++で
