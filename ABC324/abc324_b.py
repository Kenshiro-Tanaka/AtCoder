N = int(input())

flag= False
for x in range(40): # 30だとダメだった
    for y in range(40):
        if 2**x * 3**y > N:
            break
        elif 2**x * 3**y == N:
            flag = True
            break

print("NYoe s"[flag::2])


# 別解 2で割り切れるなら2で割り続けて，3で割り切れるなら3で割り続けて，結果1になればよい
# while N % 2 == 0:
#     N //= 2
# while N % 3 == 0:
#     N //= 3
# print("Yes" if N == 1 else "No")


# 2**x * 3**y <= 10**18 を満たすような整数は2**x <= 10**18 と 3**y <= 10**18より
# とりあえずはlog2(10**18)*log3(10**18) ~= 2255，実際は1178個の整数が候補
