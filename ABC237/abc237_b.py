H, W = map(int, input().split())
A = [list(input().split()) for _ in range(H)]

for i in range(W):
    B = []*H
    for j in range(H):
        B.append(A[j][i])
    print(" ".join(B))
