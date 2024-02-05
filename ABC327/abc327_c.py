A = [list(map(int, input().split())) for i in range(9)]

# 条件1つ目
for i in range(9):
    tmp = []
    for j in range(9):
        tmp.append(A[i][j])
    if len(set(tmp)) != 9:
        print("No")
        exit()

# 条件2つ目
for i in range(9):
    tmp = []
    for j in range(9):
        tmp.append(A[j][i])
    if len(set(tmp)) != 9:
        print("No")
        exit()
        
# 条件3つ目 左上から右下まで分けたgridを作る
grid = [[] for i in range(9)]
# 上段
for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        for k in range(3*i%9, 3+3*i%9, 1):
            grid[i].append(A[j][k])
# 中段
for i in range(3, 6, 1):
    for j in range(3, 6, 1):
        for k in range(3*i%9, 3+3*i%9, 1):
            grid[i].append(A[j][k])
# 下段
for i in range(6, 9, 1):
    for j in range(6, 9, 1):
        for k in range(3*i%9, 3+3*i%9, 1):
            grid[i].append(A[j][k])
            
for i in grid:
    if len(set(i)) != 9:
        print("No")
        exit()

print("Yes")
