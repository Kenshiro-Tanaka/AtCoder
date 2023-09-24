X, Y = map(int, input().split())

ans = "No"
for i in range(101): # 片方のみが存在する場合もあるから0から
    for j in range(101):
        if i+j == X and 2*i+4*j == Y:
            ans = "Yes"
            break

print(ans)
