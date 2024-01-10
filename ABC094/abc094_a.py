A, B, X = map(int, input().split())

# Bが全て犬だとするものから全て猫だとするものまでならありうる
print("YES" if A <= X <= A + B else "NO")

# 提出時は以下だがelseの時点で A <= X なので abs(A-X) = X-Aとなって上になる
# if A > X:
#     print("NO")
# else:
#     if 0 <= abs(A-X) <= B:
#         print("YES")
#     else:
#         print("NO")
