N = input()
A = list(map(int, input().split()))

A = sorted(A)
print(A[-1]-A[0]) # 並び替えれば最大値は右端-左端
