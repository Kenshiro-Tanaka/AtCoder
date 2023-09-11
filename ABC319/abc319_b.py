N = int(input())

ans = "1" # 先頭の1は確定
for i in range(1, N+1, 1):
    flag = False
    for j in range(1, 10, 1):
        if N % j == 0 and i % (N/j) == 0: # 約数なのでN/jは必ず整数
            flag = True
            break
    
    ans += str(j) if flag else "-"

print(ans)
