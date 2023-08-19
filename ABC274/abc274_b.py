H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

for j in range(W):
    cnt = 0
    for i in range(H):
        if(C[i][j] == "#"):
            cnt += 1
    print(cnt, end=" ")
