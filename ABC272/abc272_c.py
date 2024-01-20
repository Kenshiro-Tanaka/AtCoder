N = int(input())
A = list(map(int, input().split()))
sA = sorted(A)

# 偶数1個かつ奇数1個の時だけ存在しない
if N > 2:
    even = [0, 0] # どちらも2つ以上の要素が少なくとも必要なので
    odd = [-1, -1]
    for i in sA:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(max(even[-1]+even[-2], odd[-1]+odd[-2])) # 奇数+奇数の方が大きいことは当然ある
else:
    print(sum(sA) if sum(sA)%2 == 0 else -1)
