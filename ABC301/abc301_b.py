# 言われた通りに書いた解法
input() # N使わない時はこう書くのか
A = list(map(int, input().split()))

i = 0
while i < len(A)-1: # for文でやるとlen(A)が更新されなくてうまくいかない，ループ回数は未知なのでwhileでやる
    if abs(A[i] - A[i+1]) != 1:
        if A[i] < A[i+1]:
            A.insert(i+1, A[i]+1)
        else:
            A.insert(i+1, A[i]-1)
    i += 1

print(" ".join(map(str, A)))


# 別解 Aの間の数字をまるごとrangeで別の配列に入れていくからforでいける
# input()
# A = list(map(int, input().split()))

# l = []
# for i in range(len(A)-1):
#     if A[i] <= A[i+1]:
#         l += list(range(A[i], A[i+1], 1))
#     else:
#         l += list(range(A[i], A[i+1], -1))

# l.append(A[-1])

# print(*l) # *をつけてリストを渡すと要素ごとに渡される．デフォルトでは空白区切り
