X = input()

flag = False # WeakならTrue
if X[0] == X[1] == X[2] == X[3]:
    flag = True
else:
    for i in range(3):
        if int(X[i+1]) != (int(X[i])+1)%10: # 10で割った余りにすると0-9で閉じる
            flag = False # X[i+1]とint(X[i+1])は別扱いで比較がうまくいかなかった
            break
        else:
            flag = True

print("Weak" if flag else "Strong")   
