N = int(input())

ans = []
# 逆の処理を考えてN個から0個にする方法にして最後に逆にする
while N != 0: # 条件を満たす方法が必ず存在するので魔法の回数は気にしない
    if N%2 != 0:
        N -= 1
        ans.append("A")
    else:
        N //= 2
        ans.append("B")
        
ans = ''.join(list(reversed(ans)))
print(ans)
