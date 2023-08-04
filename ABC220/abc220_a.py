A, B, C = map(int, input().split())

ans = -1
for i in range(A, B+1):
    if i % C == 0:
        ans = i # breakつけて最初の候補を出力してもいい

print(ans)
