N = int(input())
# 先頭のLはA[i][0]として吸収
A = [list(map(int, input().split())) for _ in range(N)]

# setで重複消えればいいけどPythonは一次元配列だけだから調べた
A = list(map(list, set(map(tuple, A))))
print(len(A))

# 以下だとTLE
# ans = []
# for l in A:
#     if l not in ans:
#         ans.append(l)
