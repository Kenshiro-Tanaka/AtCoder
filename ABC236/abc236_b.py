N = int(input())
A = list(map(int, input().split()))

x = [0]*(N+1)  # リストが0から始まるから仕方なく +1
for i in A:
    x[i] += 1  # 各要素の個数をカウントするリスト

for j in range(1, N+1):
    if x[j] == 3:
        print(j)
        break


# こっちの方がいい別解
# total = 0
# for i in range(1, N+1):
#     total += i

# print(4*total - sum(A))


# count()はO(n)なのでTLEする
# for k in range(1, N+1):
#     a = A.count(k)
#     if a == 3:
#         print(k)
#         break
