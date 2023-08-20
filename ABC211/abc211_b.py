S = [input() for _ in range(4)]

print("Yes" if len(set(S)) == 4 else "No") # 被らなければいいから


# 最初に思いついた解法
# S = [input() for _ in range(4)]

# ans = ["H", "2B", "3B", "HR"]
# flag = True
# for i in ans:
#     if not i in S: # Sになければ
#         flag = False

# print("NYoe s" [flag::2])
