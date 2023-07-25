N = int(input())
H = list(map(int, input().split()))

print(H.index(max(H)) + 1) # 最大値を持つindexを取得，0スタートなので+1
