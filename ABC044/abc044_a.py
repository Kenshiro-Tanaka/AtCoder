N = int(input())
K = int(input())
X = int(input())
Y = int(input())

print(X*N if N <= K else X*K+Y*(N-K))
