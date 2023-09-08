N = int(input())
D = [list(map(int, input().split())) for i in range(N)]

cnt = 0
for i in range(0, N-2, 1):
    if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
        print("Yes")
        exit()

print("No")
