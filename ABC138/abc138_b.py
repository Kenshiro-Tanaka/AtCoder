N = int(input())
A = list(map(int, input().split()))

tmp = 0
for i in range(N):
    tmp += 1/A[i]

print(1/tmp)
