N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = sorted(A+B)
d = {C[i]: i for i in range(N+M)} # Cに重複が無いので C[i]: i と書ける

for i in A:
    print(d[i]+1, end=" ")
print()
for i in B:
    print(d[i]+1, end=" ")


# index()を使うとO(N)になるが，辞書を使えばO(logN)でアクセスできる
