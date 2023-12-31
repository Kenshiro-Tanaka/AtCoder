A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

ans = 0
l = [A, B, C, D, E]
l1 = [int(str(A)[-1]), int(str(B)[-1]), int(str(C)[-1]), int(str(D)[-1]), int(str(E)[-1])] # 下一桁とるために一旦str()，その後比較するのでint()に
# 下1桁が0のものから考えて，9から大きい順で
for i in range(4):
    if 0 in l1:
        ans += l[l1.index(0)]
        l1[l1.index(0)] = -1 # 用済みなので適当に-1
    else:
        ans += l[l1.index(max(l1))]
        ans += 10 - max(l1) # 10の倍数に合わせる
        l1[l1.index(max(l1))] = -1

print(ans + l[l1.index(max(l1))]) # 5個目だけ ans += 10 - max(l1) いらないので別で
