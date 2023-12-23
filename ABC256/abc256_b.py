N = int(input())
A = list(map(int, input().split()))

P = 0
grid = [0, 0, 0, 0] # マス目，駒があったら1
for i in range(N):
    grid[0] += 1
    tmp = [0, 0, 0, 0, 0, 0, 0, 0] # 4マスにしたらif文が必要になる
    for j in range(4):
        tmp[j+A[i]] = grid[j]
    P += sum(tmp[4:])
    grid = tmp[:4]

print(P)
