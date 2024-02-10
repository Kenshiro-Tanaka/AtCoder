N = int(input())
A = list(map(int, input().split()))
X = int(input())

total = sum(A)
loop = X//total # Aの和が何個分か
tmp = loop*total
for i in range(N):
    tmp += A[i]
    if tmp > X:
        print(loop*N+i+1)
        break
