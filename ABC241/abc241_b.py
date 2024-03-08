N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in B:
    if i in A:
        A.remove(i) # 同じ麺を複数の日に食べることはできない
    else:
        print("No")
        exit()

print("Yes")
