N = int(input())
D = list(map(int, input().split()))

# 月と日の各桁をリストにしたものを1つのリストにして，被りをなくした時の長さが1ならゾロ目
cnt = 0
for i in range(1, N+1, 1):
    for j in range(1, D[i-1]+1, 1):
        if len(set(list(str(i)) + list(str(j)))) == 1:
            cnt += 1

print(cnt)
