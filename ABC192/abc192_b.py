S = input()

flag = True
for i in range(len(S)):
    if i % 2 == 0: # 番目がずれることに注意，indexが偶数の時大文字ならアウト
        if 'A' <= S[i] <= 'Z':
            flag = False
            break
    else:
        if 'a' <= S[i] <= 'z':
            flag = False
            break

print("NYoe s"[flag::2])
