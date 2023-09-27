A, B, C, K = map(int, input().split())

if A >= K:
    print(K)
elif A+B >= K: # elifなので A < K が前提
    print(A)
else:
    print(A-(K-(A+B))) # 1*A + B*0 + (-1)(K-(A+B))
