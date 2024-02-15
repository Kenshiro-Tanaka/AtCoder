N = int(input())

ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    ans += b*(b+1)//2 - (a-1)*a//2
    
print(ans)


# 1からnまでの整数の和は sigma(k=1 -> n) = n(n+1)/2
# aからbまでの整数の和は sigma(k=1 -> b) - sigma(k=1 -> a-1)


# sum()を使うとTLE
# ans = 0
# for i in range(N):
#     a, b = map(int, input().split())
#     list1 = list(range(a, b+1, 1))
#     ans += sum(list1)

# print(ans)
