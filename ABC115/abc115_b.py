N = int(input())
p = [int(input()) for i in range(N)]

# 最大値だけ除いて和を求めて最大値は半分だけ足せばよい
sp = sorted(p)
print(sum(sp[:-1]) + sp[-1]//2)
