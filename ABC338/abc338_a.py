S = input()

if len(S) > 1:
    print("Yes" if 65 <= ord(S[0]) <=90 and S[1:].islower() else "No")
else:
    print("Yes" if 65 <= ord(S[0]) <=90 else "No")


# 解説に分岐を無くす考えがあった
# print("Yes" if S[0].isupper() and (len(S) == 1 or S[1:].islower()) else "No")
