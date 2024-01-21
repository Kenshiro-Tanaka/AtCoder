N = int(input())
X, Y = 0, 0
for i in range(N):
    x, y = map(int, input().split())
    X += x
    Y += y

print("Takahashi" if X > Y else "Aoki" if X < Y else "Draw")
