N = int(input())

ans = 0
for i in range(1, N+1, 2):
    yakusuu = 0
    for j in range(1, N+1, 1):
        if i%j == 0:
            yakusuu += 1
            if yakusuu == 8:
                ans += 1
            elif yakusuu > 8:
                break

print(ans)
