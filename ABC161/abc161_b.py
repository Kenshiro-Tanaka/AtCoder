N, M = map(int, input().split())
A = list(map(int, input().split()))

# 降順ソートしてM番目(1始まり)のやつが総投票数の1/4Mと比較してどうか
allvote = sum(A)
A = sorted(A, reverse=True)
print("Yes" if A[M-1] >= allvote/(4*M) else "No")
