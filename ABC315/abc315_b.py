M = int(input())
D = list(map(int, input().split()))

a, tmp = 0, 0
day = (sum(D)+1)/2 # 奇数って決まっているのが煩わしい
for i in D:
    tmp += i # dayとの比較用
    a += 1  # 月のカウント用
    if day <= tmp:
        tmp -= i
        break

print(a, int(day-tmp)) # .0ついていたらダメ
