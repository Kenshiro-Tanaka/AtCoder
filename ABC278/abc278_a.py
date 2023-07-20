N, K = map(int, input().split())
A = list(map(str, input().split()))

for i in range(K):
    A.pop(0)
    A.append('0')

print(' '.join(A)) # joinするリストの各要素は文字列である必要がある
