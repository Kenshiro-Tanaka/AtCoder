A = list(map(int, input().split()))

sA = sorted(A, reverse=True)
print(sA[0] - sA[2])
