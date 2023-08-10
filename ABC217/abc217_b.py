S1 = input()
S2 = input()
S3 = input()

S = ["ABC", "ARC", "AGC", "AHC"]
S.remove(S1)
S.remove(S2)
S.remove(S3)

print(''.join(S))


# 別解 # 答え集合から取り出して入力配列に無ければ出力して終わり
# S = [input() for _ in range(3)]

# Ans = ["ABC", "ARC", "AGC", "AHC"]
# for i in Ans:
#     if i not in S:
#         print(i)
#         break
