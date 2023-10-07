N = int(input())
A = list(map(int, input().split()))

flag = True
for i in range(N):
    if A[i]%2 == 0:
        if A[i]%3 != 0 and A[i]%5 != 0: # 「全て」なので少し面倒
            flag = False
            break

print("APPROVED" if flag else "DENIED")
