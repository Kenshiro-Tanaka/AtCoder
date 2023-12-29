# Collatz Problem
# 4, 2, 1, 4, ..., の無限ループが必ず発生することが知られている

def f(n):
    return n//2 if n%2 == 0 else 3*n+1

s = int(input())

a = s
l = [s] # 答えを保存しておいて被ったらindexを出力して終了
for i in range(1, 1000001, 1):
    a = f(a)
    if a not in l:
        l.append(a)
    else:
        print(i+1)
        exit()
