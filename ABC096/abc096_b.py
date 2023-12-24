L = list(map(int, input().split()))
K = int(input())

tmp = max(L)
x = sum(L) - tmp
print(x + (tmp<<K)) # 演算子の計算順序ルール的に括弧が必要
