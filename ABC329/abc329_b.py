N = int(input())
A = list(map(int, input().split()))

A = set(A)
A.remove(max(A))
print(max(A))
