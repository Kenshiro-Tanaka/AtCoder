N = int(input())

sum = 0
for i in range(1, N+1, 1):
    if i%3 !=0 and i%5 != 0: # 列を書いたらこれでいいことがわかる
        sum += i

print(sum)
