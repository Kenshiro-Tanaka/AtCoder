N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

for i in range(0, N, 1):
    for j in range(i+1, N, 1):
        for k in range(j+1, N, 1):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            x3 = points[k][0]
            y3 = points[k][1]
            if (x2-x1)*(y3-y1) == (y2-y1)*(x3-x1): # 2点を通る直線の方程式に残りの1点代入
                print("Yes")
                exit()

print("No")
